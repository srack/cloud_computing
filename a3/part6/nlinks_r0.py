#!/usr/bin/python

import sys


if __name__ == '__main__':
	curr_origin = ""
	hosts = {}
	for line in sys.stdin:
		line = line.rstrip()
		(origin, dest) = line.split('\t')
		if not origin == curr_origin:
			# moving onto next origin? add it if not already there 
			if not origin in hosts:
				hosts[origin] = 1
			curr_origin = origin
		# add to the list, if it is not already there
		if not dest in hosts:
			hosts[dest] = 1
	
	for h in hosts.keys():
		print h	
