#!/usr/bin/python

import sys

if __name__ == '__main__':
	for line in sys.stdin:
		line = line.rstrip()
		(count, word, dummy) = line.split()
		print word + "\t" + count
