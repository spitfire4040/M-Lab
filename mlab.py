import sys
import os
import urllib
import tarfile
import re
import shutil

counter = 0
ip_all = []
trace_all = []
ip_unique = set()
trace_unique = set()

with open("/home/jay/M-Lab/april_7") as url_list:
	for url in url_list:
		urllib.urlretrieve(url, "/home/jay/M-Lab/temp.tgz")
		tfile = tarfile.open("/home/jay/M-Lab/temp.tgz", "r:gz")
		tfile.extractall()
		for l1_filename in os.listdir("/home/jay/M-Lab/2016"):
			for l2_filename in os.listdir("/home/jay/M-Lab/2016/"+l1_filename):
				for l3_filename in os.listdir("/home/jay/M-Lab/2016/" + l1_filename+'/' + l2_filename):
					for l4_filename in os.listdir("/home/jay/M-Lab/2016/" + l1_filename+'/' + l2_filename + '/' + l3_filename):
						with open("/home/jay/M-Lab/2016/" + l1_filename +'/' + l2_filename + '/' + l3_filename + '/' + l4_filename, 'r') as f:
							trace = []
							for line in f:
								line = line.split()
								for x in range(1, 31):
									try:
										if line[0] == str(x):
											if line[4] != None:
												address = line[4]
												address = address.strip('()')
												ip_all.append(address + '\n')
												ip_unique.add(address + '\n')												
												trace.append(address)
									except:
										pass
							trace = ' '.join(trace)
							trace_all.append(trace + '\n')
							trace_unique.add(trace + '\n')


		if os.path.exists("/home/jay/M-Lab/2016"):
			shutil.rmtree("/home/jay/M-Lab/2016")

		if os.path.exists("/home/jay/M-Lab/temp.tgz"):
			os.remove("/home/jay/M-Lab/temp.tgz")

		counter += 1
		os.system('clear')
		print counter				

outfile = open("april_7_all_ip", "w")
for item in ip_all:
	outfile.write(item)
outfile.close()

outfile = open("april_7_all_trace", "w")
for item in trace_all:
	outfile.write(item)
outfile.close()

outfile = open("april_7_unique_ip", "w")
for item in ip_unique:
	outfile.write(item)
outfile.close()
outfile = open("april_7_unique_trace", "w")
for item in trace_unique:
	outfile.write(item)
outfile.close()

outfile = open("april_7_stats", "w")
outfile.write("Total IP: " + str(len(ip_all)) + '\n')
outfile.write("Unique IP: " + str(len(ip_unique)) + '\n')
outfile.write("Total Trace: " + str(len(ip_unique)) + '\n')
outfile.write("Unique Trace: " + str(len(trace_unique)) + '\n')
outfile.close()