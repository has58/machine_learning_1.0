# AUTHOR: HAIDER ALI SIDDIQUEE
# DATE  : 2/15/2020
# TIME  : 4:59:01
# ABOUT : IMPLEMENTATION OF GRADIENT DESCENT FOR SQUARES

import sys
import math
import random
datafile = sys.argv[1]
f = open (datafile, 'r')
data = []
i = 0
l = f.readline()

######################
##### READ DATA ######
######################

while (l != ''):
	a = l.split()
	# here 'a' is a list that store one column data like ['4.3','5.4','6']
	# And we are taking l2 to store floating numbers in our string like [4.3,5.4,6]
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
f = open (labelfile, 'r')
traininglabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
	a = l.split()
	traininglabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1
#print(n)

###########################
###### INITIALINING W #####
###########################

w = []
for i in range(0, cols, 1):
	w.append(0.2*random.random() - 0.01)
#print(w)

##################################
###### DOT PRODUCT FUNCTION  #####
##################################

def dot_product(m1, m2):
	result = 0
	for j in (0, cols, 1):
		result += m1[j]*m2[j]
	return result

#####################################
###### GRADIENT DECENT ITRATION #####
#####################################

eta = 0.0001
diff = 1
error = rows + 10
count = 0
while(diff > 0.001):
	dellf = []
	for m in range(0, cols, 1):
		dellf.append(0)
	for j in range (0, rows, 1):
		if (traininglabels.get(str(j)) != None):
			dot_pro = dot_product(w, data[j])
			for k in range(0, cols, 1):
				dellf[k] += (traininglabels.get(str(j)) -
				dot_pro)*data[j][k]
#print(dellf)

	######################
	###### UPDATE W  #####
	######################
	
	for j in range (0, cols, 1):
		w[j] += eta*dellf[j]
	prev=error
	error= 0
        
	##########################
	###### Compute Error #####
	##########################

	for j in range(0, rows, 1):
		if(traininglabels.get(str(j)) != None):
			error += (traininglabels.get(std(j)) - dot_product(w, data[j]))**2
	if (prev > error):
		diff = prev - error
	else:
		diff = error - prev
	count += 1
	if (count%100 == 0):
		print(error)
#print("ERROR = " + str(error))


normw = 0
for i in range(0, (cols - 1), 1):
	normw += w[i]**2
	#print("W", w)

normw = math.sqrt(normw)

d_original = abs(w[len(w) - 1]/normw)
#print (d_original)
	
##############################
###### LABELS PREDICTION #####
##############################

for i in range(0, rows, 1):
	if(traininglabels.get(i) == None):
		dot_pro = dot_product(w, data[i])
		if(dot_pro > 0):
			print ("1" + str(i))
		else:
			print("0" + str(i))
