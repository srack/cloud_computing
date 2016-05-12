#!/usr/bin/python

import sys

if __name__ == '__main__':
	for line in sys.stdin:
		line = line.rstrip()
		(count, pair, dummy) = line.split()
		print pair + "\t" + count
