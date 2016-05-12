#!/usr/bin/python

import sys

if __name__ == '__main__':
	curr_host_checking = ""
	hosts_referenced = {}
	for line in sys.stdin:
		line = line.rstrip()
		(host_checking, host) = line.split('\t')
		if host_checking == curr_host_checking:
			# add to the list, if it is not already there
			if not host in hosts_referenced:
				hosts_referenced[host] = 1
		else:
			# moving onto the next word? print the previous
			if not curr_host_checking == "":
				print curr_host_checking + ': ' + str(hosts_referenced.keys())
			curr_host_checking = host_checking
			hosts_referenced = {}
			hosts_referenced[host] = 1
			
	print curr_host_checking + ': ' + str(hosts_referenced.keys())
