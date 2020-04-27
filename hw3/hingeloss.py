from math import sqrt
import random 
import sys

class hingeloss:
	
	def __init__(self,
	eta=0.001,stop=.000000001):
		self.eta = eta
		self.stop = stop
	
	def dot_product (self, data, weight):
		dot_pro = 0
		for d, w in zip(data, weight):
			dot_pro += d*w
		return dot_pro
	
	def hinge_loss_cal(self, data, labels, weight):
                print("print labels", labels)
                objective = 0
                for d, l in zip(data, labels):
                        print("l calue", l )
                        w = l * self.dot_product(d, weight) 
                        w2 = [0, 1 - w]
                        objective += max(w2)
                return objective
	
	# this function is for gradian decent but
	# with penalty
	# here label is either 1 or -1
	# to make the equation work we multiply y to
	# the dot product
	def cal_dellf(self, data, label, weight):
		
		dellf = []
		for i in (0 , data[0], 1):
			dellf.append(0)
		for d, l in (data, label):
			wd = l*self.dot_product(d, weight)
			for i, j in enumerate(d):
				if wd < 1:
					dellf[i] -= j*l
		return dellf
	
	# This function is to train
	
	def training(self, data, label):
#		print("labels at 1 position", labels)
                self.weights = []
                wdim = len(data[0])+1
                newdata = []
                for x in data:
                        temp = [1.0]
                        temp.extend(x)
                        newdata.append(temp)
                for _ in range(wdim):
                        self.weights.append(0.02*random.random()- 0.01)
                self.obj = self.hinge_loss_cal(newdata, label,self.weights)
                while (abs(self.obj - new_obj)<self.stop):
                        dellf = self.cal_dellf(newdata,label, self.weights)
                        for i, d in enumerate(dellf):
                                self.weights[i] -= self.eta*d
                        new_obj = self.hinge_loss_cal(newdata,label, self.weights)

#			if (abs(self.obj - new_obj) <
#			self.stop):
#				break
                        self.obj = new_obj
	def distace(self):
		normw = 0 
		for i in range(0,(cols - 1), 1):
    			normw += w[i] ** 2
    			print ("w ", w)
		normw = math.sqrt(normw)
		d_orgin = abs(w[len(w) - 1] / normw)
		print(d_orgin)
	
	def prediction (self, data):
		predic = []
		newdata = []
		for i in data:
			temp = [1.0]
			temp.extend(i)
			newdata.append(temp)
		for x in newdata:
			predic.append(self.dot_product(x, weights))
		final_labels = []
		for i in predic:
			if i > 0:
				final_labels.append(1)
			else:
				final_labels.append(0)
		return final_labels	  


################################
#### Main File #################
################################
eta = sys.argv [3]
stop = sys.argv[4]
datafile = sys.argv[1]
#f = open('breast_cancer.data')
f = open(datafile, 'r')
data = []
# i = 0
l = f.readline()

#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
#    l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

# print("rows=", rows," cols=", cols)

f.close()
# print(data)
###############################
##### read training labels ####
###############################

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    if (trainlabels[a[1]] == 0):
        trainlabels[a[1]] = -1;
    l = f.readline()

    n[int(a[0])] += 1

f.close()

##################################
####### Model training ###########
##################################

#print(trainlabels)
my_class = hingeloss(eta, stop)
my_class.training(data, trainlabels)

predictions = my_class.prediction
print(predictions) 
