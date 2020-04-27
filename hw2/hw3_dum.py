import sys
import random
import math

datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
l = f.readline()
#################
### hinge loss ##
#################
def hinge_loss_cal(self, data, label,
	weight):
    objective = 0
    for d, l in zip(data, labels):
        w = l*self.dot_product(d,
			weights):
        w2 = [0, 1 - temp]
        objective += max(w2)
    return objective

###########################
##### calculate dellf######
###########################
def cal_dellf(self, data, label, weight):
    dellf = []
    for i in (0 , data[0], 1):
        dellf.append(0)
    for d, l in (data, label):
        w = l*self.dot_product(d, weight)
	for i, d in enumerate(d):
            if temp < 1:
                dellf[i] -= d*y
    return dellf
#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()
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
    #    trainlabels_size[a[0]] = trainlabels_size[a[0]]+1
    if (trainlabels[a[1]] == 0):
        trainlabels[a[1]] = -1;
    l = f.readline()

    n[int(a[0])] += 1

f.close()
# print(trainlabels)
##################################
########## initialize w ##########
##################################
# print("this is new code")
w = []
for j in range(0, cols, 1):
    # print(random.random())
    w.append(0.02 * random.random() - 0.01)


# print(w)

#####################################
#### calculation of doc product #####
#####################################

def dot_product(data, weights):
    dot_pro = 0
    for i in range(0, cols, 1):
        dot_pro += data[i] * weights[i]
    return dot_pro


#######################################
##### gradient descent iteration ######
#######################################

eta = 0.001
error = rows + 10
diff = 1
count = 0
# for i in range(0, 1500, 1):
while ((diff) > 0.000000001):
    dellf = cal_dellf(data[j], trainlabels[j], w)

    ##########################
    ####### update w #########
    ##########################

    for j in range(0, cols, 1):
        w[j] = w[j] + eta * dellf[j]

    prev = error
    error = 0

    ############################
    #### compute error #########
    ###########################

    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            # print(dot_product(w,data[j]))
            error += (trainlabels.get(str(j)) - dot_product(w, data[j])) ** 2
    if (prev > error):
        diff = prev - error
    else:
        diff = error - prev
    count = count + 1
    if (count % 100 == 0):
        print(error)

print ("error = " + str(error))

# print("w= ")
normw = 0
for i in range(0, (cols - 1), 1):
    normw += w[i] ** 2
    print ("w ", w)

# print("")

# normw = (normw)**0.5
normw = math.sqrt(normw)
# print("sqrt")
# print("||w||="+str(normw))
# print("")

d_orgin = abs(w[len(w) - 1] / normw)

#print ("Distance to origin = " + str(d_orgin))

#################################
###### calc of prediction #######
#################################

for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) == None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("1 " + str(i))
        else:
            print("0 " + str(i))
