import sys
import os

count = 1

inf = open("april_gs", "r")
outf = open("mlab_april", "w")

for line in inf:
	line = line.replace('gs://', 'https://storage.googleapis.com/')
	outf.write(line)
