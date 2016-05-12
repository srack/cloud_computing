#!/usr/bin/python

import sys
import os
import string
import subprocess

if __name__ == '__main__':
	#os.system("whatever command i want")

	# first remove any of the output files that might already exist
	os.system("hadoop fs -rm -r /users/srack/nlinks_output*")

	output_count = 1
	init_cmd = "hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar " 
	mapper_opts = "-mapper nlinks_m0.py " + "-file nlinks_m0.py " 
	reducer_opts = "-reducer nlinks_r0.py " + "-file nlinks_r0.py " 
	

	# start by just running it on nd.edu file
	jar_cmd = init_cmd
	jar_cmd += "-input /public/www/nd.edu "
	jar_cmd += "-output /users/srack/nlinks_output" + str(output_count) + " "
	jar_cmd += mapper_opts
	jar_cmd += reducer_opts

	os.system(jar_cmd)

	num_hosts = 1

	# get all existing html files and write them to a file for later 
	pipe0 = os.popen("hadoop fs -ls /public/www/")
	s0 = open("hosts_avail.tmp", 'w')
	s0.write(pipe0.read())
	s0.close()
	
	
	# need to perform the rest of this until convergence
	while 1:
		jar_cmd = init_cmd

		# pull out the hosts output_count away from nd.edu
		# these will be the inputs
		pipe1 = os.popen("hadoop fs -cat /users/srack/nlinks_output" + str(output_count) + "/part-00000")
		# increase the output_count
		output_count += 1

		s1 = open("file.tmp", 'w')
		s1.write(pipe1.read())
		s1.close()
		hosts = open("file.tmp", 'r')
		

		new_num_hosts = 0
		for line in hosts:
			line = line.rstrip()
			if not line == "":
				pipe2 = subprocess.Popen(('cat', 'hosts_avail.tmp'), stdout=subprocess.PIPE)
				pipe3 = subprocess.Popen(('grep', "/www/" + line + "$"), stdin=pipe2.stdout, stdout=subprocess.PIPE)
				blah = pipe3.communicate()[0]
				if not blah == "":
					jar_cmd += "-input /public/www/" + line + " "
					new_num_hosts += 1
		hosts.close()
		os.system("rm file.tmp")
		
		print "\nCalculating " + str(output_count) + "-links\n\tNumber of hosts found so far = " + str(new_num_hosts) + "\n"
		
		if new_num_hosts == num_hosts:
			break

		num_hosts = new_num_hosts

		jar_cmd += "-output /users/srack/nlinks_output" + str(output_count) + " "
		jar_cmd += mapper_opts
		jar_cmd += reducer_opts
	
		# run the next round
		os.system(jar_cmd)
	print "\nfinished! " + str(output_count-2) + " degrees of separation"
	os.system("rm hosts_avail.tmp")
