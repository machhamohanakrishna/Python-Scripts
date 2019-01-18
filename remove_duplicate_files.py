
# This script will recursively go over the give path and deletes the duplicate files. It also gives the list of deleted duplicate files. 

import os
import sys
import hashlib
file_dic = {}
dup = {}
for root,directories,filenames in os.walk('Path_file'):
	for file in filenames:
		actual_file = os.path.join(root,file)
		f = open (actual_file, 'r')
		data = f.read()
		md5_hash = hashlib.md5(data).hexdigest()
		if md5_hash in file_dic:
			dup[md5_hash] = actual_file
			os.remove(actual_file)
		else:
			file_dic[md5_hash] = actual_file
print file_dic
print dup
