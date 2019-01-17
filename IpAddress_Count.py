import re
from collections import Counter
from datetime import datetime
startTime = datetime.now()

list_ip_address = []
file = open("Path_to_file", "r")
for line in file:       
        ip = re.search(r'[0-9]+(?:\.[0-9]+){3}', line)
        ipaddress = ip.group()
        list_ip_address.append(ipaddress)
Count_IP=Counter(list_ip_address)

for ip in Count_IP:
    print ip, Count_IP[ip]
print(datetime.now() - startTime)
