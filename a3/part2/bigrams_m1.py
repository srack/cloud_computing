#!/usr/bin/python

import sys

if __name__ == '__main__':
	# 1 pair with count per line
	for line in sys.stdin:
		line = line.rstrip()
		(pair, count) = line.split("\t")
		print count + " " + pair + "\t" + "1"
