#!/usr/bin/python

import sys
import string
import re

class hth:
	def execute(self):
		print_str = ""
		# make a list to keep track of the hosts that a page references
		#  note: get ride of repeats along the way
		hosts = []	
		# reading html on stdin
		for line in sys.stdin:
			# find the next <a> tag, look for href within the tag
			m = re.search('\<a.*? href=\"(?P<url>.+?)\"', line)
			if m != None:
				url = m.group("url")
				if url.startswith("http"):
					# add the top-level directory to it if does not yet exist
					n = re.search('(?P<top>.+?\.(edu|org|gov)).*', url)
					top_level = n.group("top") 
					add = True
					# presumably, the hosts list won't get too long so a linear
					#  search shouldn't be too inefficient
					for host in hosts:
						if host == top_level:
							add = False
							break
					if add:
						hosts.append(top_level)
		# create string with all hosts found
		for host in hosts:
			print_str += host + "\n"
		return print_str

if __name__ == '__main__':
	h = hth()
	print h.execute()
