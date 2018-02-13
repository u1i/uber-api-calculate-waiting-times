import json
import pylab
import random
import math

seconds=[]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def myround(x, base=50):
    return int(base * round(float(x)/base))

with open('uber.json') as json_data:
	d = json.load(json_data)

	trip_num = 1

	for trip in d["history"]:
		rtime = trip["request_time"]
		stime = trip["start_time"]
		wait = stime - rtime
		# print "Trip " + str(trip_num) + ": " +  str(wait) + " seconds"
		# print stime, rtime
		print str(trip_num) + "," + str(myround(wait))
		trip_num = trip_num + 1
		seconds.append(wait)

print "Average waiting time: " +str(mean(seconds))
