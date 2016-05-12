import sys
import os
import string
import Queue

fn_default = "jobs.db"

## class: JobsDatabase ##
class JobsDatabase():
	# schema -- JOB_ID,STATUS
	# status possible values:
	#	0 = WAITING
	#	1 = RUNNING
	#	2 = DONE
	# job_id of an entry will never change, status will only change between 0,1,2

	# function: init()
	def __init__(self, filename = fn_default):
		self.fn = filename
		self.db = {}
		self.next_job_id = 0

		# array indicates number of jobs in each status
		# 	self.num_in_status[0] = number of jobs in WAITING state
		#	self.num_in_status[1] = number of jobs in RUNNING state
		# 	self.num_in_status[2] = number of jobs in DONE state
		self.num_in_status = [0] * 3

		# create a queue of waiting jobs		
		self.waiting_jobs = Queue.Queue()

		# if the file exists already, load what we have into self.db
		if os.path.isfile(self.fn):
			f = open(self.fn)
			for line in f:
				comps = line.split(",")
				job_id = int(comps[0])
				status = int(comps[1])
				self.db[job_id] = status
				if job_id >= self.next_job_id:
					self.next_job_id = job_id + 1
				# increment appropriate count
				self.num_in_status[status] = self.num_in_status[status] + 1
				if status == self.status_str_to_num("WAITING"):
					self.waiting_jobs.put(job_id)

	# function: create_record()
	def create_job(self):
		f = open(self.fn, 'a')
		# a created job will always be initialized to WAITING state (= 0)
		f.write(self.get_next_job_id_str() + "," + "0" + "\n") 
		self.db[self.next_job_id] = 0
		# add to the waiting queue
		self.waiting_jobs.put(self.next_job_id)
		self.next_job_id = self.next_job_id + 1
		f.close()

	# function: get_next_job_id_str()
	def get_next_job_id_str(self):
		# formatted string so each job id is a string with 7 chars
		return "%07d" % self.next_job_id

	
	# function: change_job_status()
	def change_job_status(self, job_id, new_status):
		# error checks
		if not job_id in self.db:
			print "error: job to change not in db"
			sys.exit(1)
		if not new_status == 0 and not new_status == 1 and not new_status == 2:
			print "error: status must be 0, 1, or 2"
			sys.exit(1) 

		# update counts of statuses
		self.num_in_status[self.db[job_id]] = self.num_in_status[self.db[job_id]] - 1
		self.num_in_status[new_status] = self.num_in_status[new_status] + 1

		# update it in db
		self.db[job_id] = new_status

		# then have to update it in the existing file
		# each line is 10 bytes -- 
		#	7 chars for job_id
		#	1 char for ,
		#	1 char for status (0, 1, 2)
		#	1 char for \n
		f = open(self.fn, 'r+')
		
		# since the db will start with job_id = 0 and increment by 
		#  1 each time, can find position of a specific job_id quickly
		# job_id * 10 bytes gives line number
		f.seek(job_id*10 + 8)
		f.write(str(new_status))
		f.close()

	# function: status_str_to_num()
	def status_str_to_num(self, status_str):
		if status_str.upper() == "WAITING":
			return 0
		elif status_str.upper() == "RUNNING":
			return 1
		elif status_str.upper() == "DONE":
			return 2
		else:
			print "error: status string must be WAITING, RUNNING, or DONE"
			sys.exit(1)

	# function: get_status_of_job()
	def get_status_of_job(self, job_id):
		if not job_id in self.db:
			print "error: job not in db"
			sys.exit(1)
		return self.db[job_id]

	# function: get_num_jobs_in_status()
	def get_num_jobs_in_status(self, status):
		return self.num_in_status[status]

	# function: set_next_job_as_running()
	# notes: returns job_id string for process that was just set to RUNNING
	def set_next_job_as_running(self):
		# this will return the lowest job_id of a process that is WAITING
		next_job = self.waiting_jobs.get()
		self.change_job_status(next_job, self.status_str_to_num("RUNNING"))
		return "%07d" % next_job

## main for testing purposes ##
if __name__ == "__main__":
	db = JobsDatabase()
	db.create_job()
	db.create_job()
	db.change_job_status(1, db.status_str_to_num("DONE"))
	print db.get_num_jobs_in_status(db.status_str_to_num("WAITING"))
