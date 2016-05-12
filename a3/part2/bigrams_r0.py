#!/usr/bin/python

import sys

if __name__ == '__main__':
	curr_key= ""
	count = 0
	for line in sys.stdin:
		line = line.rstrip()
		key = line.split('\t')[0]
		if key == curr_key:
			count += 1
		else:
			if not count == 0:
				print curr_key + '\t' + str(count)
			count = 1
			curr_key = key
	print curr_key + '\t' + str(count)
