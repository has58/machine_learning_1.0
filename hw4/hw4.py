import sys
import random
import math
'''
If you want to use eta from argument please remove # from line 12 and 13
Thank You 
'''

datafile = sys.argv[1]
labelfile = sys.argv[2]
eta = 0.01
stop = 0.001
#eta = float(sys.argv[3])
#stop = float(sys.argv[4])


def sigmoid(data, weights):
  return (1/(1+math.exp(-1*dot_product(data, weights))))

f = open(datafile, 'r')
data = []
l = f.readline()

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
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
f.close()

##################################
########## initialize w ##########
##################################

w = []
for j in range(0, cols, 1):
    w.append(0.02 * random.random() - 0.01)

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
error = rows + 10
diff = 1
count = 0
while (diff > stop):
    dellf = []
    for m in range(0, cols, 1):
        dellf.append(0)
    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            for k in range(0, cols, 1):
                log_reg = (trainlabels.get(str(j)) - sigmoid(data[j], w))
                dellf[k] += (log_reg)*data[j][k]
    ##########################
    ####### update w #########
    ##########################

    for j in range(0, cols, 1):
        w[j] = w[j] + eta * dellf[j]

    prev = error
    error = 0
    obj=0

    ############################
    #### compute error #########
    ###########################

    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
#          obj += math.log(1 + math.exp((-1 * (trainlabels.get(str(j)))) * (dot_product(w, data[j]))))
          obj += -1*trainlabels.get(str(j))*math.log(sigmoid(data[j], w)) + ((1-trainlabels.get(str(j)))*(math.log(1-sigmoid(data[j],w))))  
    error = obj
    if (prev > error):
        diff = prev - error
    else:
        diff = error - prev
    count = count + 1
    if (count % 100 == 0):
        print(error)

#print ("error = " + str(error))

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

print ("Distance to origin = " + str(d_orgin))

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

