#!/usr/bin/python

import sys

if __name__ == '__main__':
	curr_word = ""
	hosts = {}
	for line in sys.stdin:
		line = line.rstrip()
		(word, host) = line.split('\t')
		if word == curr_word:
			# add to the list, if it is not already there
			if not host in hosts:
				hosts[host] = 1
		else:
			# moving onto the next word? print the previous
			if not curr_word == "":
				print curr_word + ': ' + str(hosts.keys())
			curr_word = word
			hosts = {}
			hosts[host] = 1
			
	print curr_word + ': ' + str(hosts.keys())
