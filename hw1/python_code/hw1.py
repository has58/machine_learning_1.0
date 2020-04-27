# AUTHOR: HAIDER ALI SIDDIQUEE
# DATE  : 01/08/2020
# TIME  : 4:07:01
# ABOUT : NAIVE BAYES CLASSIFIER


import sys
import math


datafile = sys.argv[1]
f = open (datafile, 'r')
data = []
i = 0
l = f.readline()


######################
##### READ DATA ######
######################

while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()
rows = len(data)
cols = len(data[0])

#print(rows)
#print(cols)

########################
###### READ LABELS #####
########################
labelfile = sys.argv[2]
f= open (labelfile, 'r')
traininglabels = {}
n = [0, 0]
l = f.readline()
while(l != ''):
	b = l.split()
	traininglabels[int(b[1])] = int(b[0])
	l = f.readline()
	n[int(b[0])] += 1 

#######################
#####COMPUTE MEAN #####
#######################
m0 = []
for j in range(0,cols,1):
	m0.append(0.01)
m1 = []
for j in range(0, cols, 1):
	m1.append(0.01)

for i in range(0, rows, 1):
	if(traininglabels.get(i) != None and traininglabels[i] == 0):
		for j in range(0, cols, 1):
			m0[j] += data[i][j]
	if(traininglabels.get(i) != None and traininglabels[i] == 1):
		for j in range(0, cols, 1):
			m1[j] += data[i][j]
for j in range(0, cols, 1):
	m0[j] = m0[j]/n[0]
	m1[j] = m1[j]/n[1]

'''
####################################
##### Classify unlabled points #####
#####  by Nearest mean Method  #####
####################################
for i in range(0, rows, 1):
	if (traininglabels.get(i) == None):
		d0 = 0 
		d1 = 0
		for j in range(0, cols, 1):
			d0 += (m0[j] - data[i][j])**2
			d1 += (m1[j] - data[i][j])**2
		if (d0<d1):
			print("0", i)
		else:
			print("1", i)
'''
###############################
###### STANDARD DEVIATION #####
###############################
s0 = []
s1 = []
for j in range(0, cols, 1):
	s0.append(0)
	s1.append(0)
for i in range(0, rows, 1):
	if (traininglabels.get(i) != None and traininglabels[i] == 0):
		for j in range(0, cols, 1):
			s0[j] += (data[i][j] - m0[j])**2
	if (traininglabels.get(i) != None and traininglabels[i] == 1):
		for j in range(0, cols, 1):
		 	s1[j] += (data[i][j] - m1[j])**2
for j in range(0, cols, 1):
	s0[j] = (s0[j]/n[0])**(0.5)
	s1[j] = (s1[j]/n[1])**(0.5)
#print(s0)
#print(s1)
###################################
##### Classify unlabled point #####
#####  by naive bayes Algo.   #####
###################################
for i in range(0, rows, 1):
	if(traininglabels.get(i) == None):
		c0 = 0
		c1 = 0
		for j in range(0, cols, 1):
			c0 += ((data[i][j] - m0[j])/s0[j])**2
			c1 += ((data[i][j] - m1[j])/s1[j])**2
		if (c0 < c1):
			print("0", i)
		else:
			print("1", i)
