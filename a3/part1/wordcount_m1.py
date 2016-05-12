#!/usr/bin/python

import sys

if __name__ == '__main__':
	# 1 word with count per line
	for line in sys.stdin:
		(word, count) = line.split()
		print count + " " + word + "\t" + "1"
