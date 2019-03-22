
# This script will continously monitor the whether there is any change in the IP address for the domain pointing to load balancer.
# If there is any change, it will print out a message and share the new IP's.


import os
import time
import re
import subprocess

Current_IP = []

while 1:

	IP = subprocess.Popen(["dig xxxxxxxx.com +short"],stdout=subprocess.PIPE, shell=True)
	(out,err) = IP.communicate()
	New_IP = re.findall('[0-9]+(?:\.[0-9]+){3}',out)
	#print New_IP
	if (set(Current_IP) != set(New_IP)):
		if (Current_IP == []): 
			print "This is the first time iteration"
			Current_IP = New_IP
		else:
			print "The IP has changed and the New IP is :" + str(New_IP)
			Current_IP = New_IP
	time.sleep(20) 
