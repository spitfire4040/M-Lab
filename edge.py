import sys
import os

# initialize lists
edgeList = set()
starCounter = 1
count = 1

f = open("/home/jay/M-Lab/april_7_unique_trace", "r")
for item in f:

	# set list so it will reset
	trace = []

	# split trace and push to list
	for item in item.split():
		trace.append(item)

	# find length of list
	length = len(trace)

	# set iterator variable so it will reset
	i = 0

	# iterate through trace list for pairs
	while i < length - 1:
		first = trace[i]
		second = trace[i+1]

		# add to edgeList set (unique values only)
		edgeList.add(str(first) + ' ' + str(second))
		i += 1


# write edgeList to file
out = open("/home/jay/M-Lab/april_7_edge", "w")
for item in edgeList:
	out.write(item + '\n')


# close file
f.close()
out.close()