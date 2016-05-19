import sys
import os

unique_ip = set()
unique_trace = set()
unique_edge = set()

for x in range(1,8):
	infile1 = open("/home/jay/M-Lab/april_" + str(x) + "_unique_ip", "r")
	infile2 = open("/home/jay/M-Lab/april_" + str(x) + "_unique_trace", "r")
	infile3 = open("/home/jay/M-Lab/april_" + str(x) + "_edge", "r")

	for item in infile1:
		unique_ip.add(item)

	for item in infile2:
		unique_trace.add(item)

	for item in infile3:
		unique_edge.add(item)

	infile1.close()
	infile2.close()
	infile3.close()

out = open("cumulative 1-7", "w")
out.write("Total IPs: " + str(len(unique_ip)) + '\n')
out.write("Total Traces: " + str(len(unique_trace)) + '\n')
out.write("Total Edges: " + str(len(unique_edge)) + '\n')
out.close()