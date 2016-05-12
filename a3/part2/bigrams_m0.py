#!/usr/bin/python

import sys
import string
import re

def htmltowords():
	print_str = ""
	# reading html on stdin
	for line in sys.stdin:
		# find the next <a> tag, look for href within the tag
		line = line.rstrip()
		line = string.lower(line)
		comp = re.split('[^a-z]', line)
		for c in comp:
			if len(c) > 3:
				print_str += c + "\n"
	return print_str

if __name__ == '__main__':
	# note -- assumes that order matters for bigrams
	prev_word = ""
	words = (htmltowords()).split("\n")
	for word in words:
		if not prev_word == "":
			print prev_word + "," + word + "\t1"
		prev_word = word
