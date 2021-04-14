#!/usr/bin/python

import requests
#import random
#from time import sleep


r = requests.get("http://api.thingspeak.com/update?api_key=XXXXXXXXXXXXXXXXXXXXXX&field1=0")


'''
my_key = "XXXXXXXXXXXXXXXXXXXX"
my_value = random.randint(-5000, 5000)
url = "http://api.thingspeak.com/update?api_key="+my_key+"&field1="+str(my_value)

r = requests.get(url)
'''

print (r.json())

