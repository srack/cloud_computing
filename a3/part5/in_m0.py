#!/usr/bin/python

import sys
import os
import string
import re

def htmltohosts():
	print_str = ""
	# make a list to keep track of the hosts that a page references
	#  note: get ride of repeats along the way
	hosts = {}	
	# reading html on stdin
	for line in sys.stdin:
		# find the next <a> tag, look for href within the tag
		m = re.search('\<a.*? href=\"(?P<url>.+?)\"', line)
		if m != None:
			url = m.group("url")
			if url.startswith("http") or url.startswith("www"):
				# add the top-level directory to it if does not yet exist
				n = re.search('(https?://)?(www\.)?(?P<top>.+?\.(edu|org|gov)).*', url)
				if not n == None:
					top_level = n.group("top")
					if not top_level in hosts:
						hosts[top_level] = 1
	# create string with all hosts found
	for host in hosts:
		print_str += host + "\n"
	return print_str

if __name__ == '__main__':
	hosts_referenced = (htmltohosts()).split("\n")
	fn = os.environ['mapreduce_map_input_file']
	host_checking = fn[(string.find("www/", fn)+4):] 

	match = re.search(".+?/www/(?P<host>.+)", fn)
	host_checking = match.group("host")
	for hr in hosts_referenced:
		if not hr == "":
			print hr + "\t" + host_checking 
