#!/usr/bin/python

import sys

if __name__ == '__main__':
	# 1 word per line
	curr_word = ""
	count = 0
	for line in sys.stdin:
		line = line.rstrip()
		word = line.split('\t')[0]
		if word == curr_word:
			count += 1
		else:
			if not count == 0:
				print curr_word + '\t' + str(count)
			count = 1
			curr_word = word
	print curr_word + '\t' + str(count)
