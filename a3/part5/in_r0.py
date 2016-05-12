#!/usr/bin/python

import sys

if __name__ == '__main__':
	curr_host_dest = ""
	hosts_referenced = {}
	for line in sys.stdin:
		line = line.rstrip()
		(host_dest, host) = line.split('\t')
		if host_dest == curr_host_dest:
			# add to the list, if it is not already there
			if not host in hosts_referenced:
				hosts_referenced[host] = 1
		else:
			# moving onto the next word? print the previous
			if not curr_host_dest == "":
				print curr_host_dest + ': ' + str(hosts_referenced.keys())
			curr_host_dest = host_dest
			hosts_referenced = {}
			hosts_referenced[host] = 1
			
	print curr_host_dest + ': ' + str(hosts_referenced.keys())
