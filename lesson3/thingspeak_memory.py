#!/usr/bin/python
import requests
import subprocess
from time import sleep



my_key = "XXXXXXXXXXXXXXXXXX"
cmd_free = 'free -m | awk \'FNR==2 {print $4}\''
cmd_used = 'free -m | awk \'FNR==2 {print $3}\''

free_mem = subprocess.check_output(cmd_free, shell=True)[:-1]
used_mem = subprocess.check_output(cmd_used, shell=True)[:-1]
print ("free memory:", int(free_mem))
print ("used memory:", int(used_mem))

url = "http://api.thingspeak.com/update?api_key="+my_key+"&field3="+str(free_mem)+"&field4="+str(used_mem)

r = requests.get(url)

print(r.json())