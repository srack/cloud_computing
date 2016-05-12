#!/usr/bin/python

import sys
import os
import string
import re

def htmltowords():
	print_str = ""
	# reading html on stdin
	for line in sys.stdin:
		line = line.rstrip()
		line = string.lower(line)
		comp = re.split('[^a-z]', line)
		for word in comp:
			if len(word) > 3:
				print_str += word + "\n"
	return print_str

if __name__ == '__main__':
	words = (htmltowords()).split("\n")
	for word in words:
		if not word == "":
			fn = os.environ['mapreduce_map_input_file']
			match = re.search(".+?/www/(?P<host>.+)", fn)
			print word + "\t" + match.group("host") 
