import sys
import random
import math

datafile = sys.argv[1]

f = open(datafile, 'r')
data = []
a = f.readline()

while (a != ''):
    b = a.split()
    a2 = []
    for c in range(0, len(b), 1):
        a2.append(float(b[c]))
    data.append(a2)

    a = f.readline()

rows = len(data)
cols = len(data[0])

f.close()


d = int(sys.argv[2])

col = [0 for _ in range(0, cols, 1)]

e = [col for _ in range(0, d, 1)]

value = 0

for f in range(0, d, 1):
    value = random.randrange(1, rows-1)
    e[f] = data[value]

trainlabels = {}
difference = 1

prev = [[0]*cols for g in range(d)]
mdist = [0 for _ in range(0, d, 1)]

n = [0.1 for _ in range(0, d, 1)]
dist = [0.1 for _ in range(0, d, 1)]

totaldist = 1
classe = []

while ((totaldist) > 0):
    for h in range(0,rows, 1):
        dist =[]

        for f in range(0, d, 1):
            dist.append(0)

        for f in range(0, d, 1):
            for c in range(0, cols, 1):
                dist[f] += ((data[h][c] - e[f][c])**2)

        for f in range(0, d, 1):
            dist[f] = (dist[f])**0.5

        mindist=0
        mindist = min(dist)
        for f in range(0, d, 1):
            if(dist[f]==mindist):
                trainlabels[h] = f
                n[f]+=1
                break

    e = [[0]*cols for g in range(d)]
    col = []

    for h in range(0, rows, 1):
        for f in range(0, d, 1):
            if(trainlabels.get(h) == f):
                for c in range(0, cols, 1):
                    temp =  e[f][c]
                    temp1 =  data[h][c]
                    e[f][c] = temp + temp1
    for c in range(0, cols, 1):
        for h in range(0, d, 1):
            e[h][c] = e[h][c]/n[h]

    classe = [int(g) for g in n]
    n=[0.1]*d
   #print("m",e)
    
    mdist = []
    for f in range(0, d, 1):
        mdist.append(0)
    for f in range(0, d, 1):
        for c in range(0, cols, 1):
            mdist[f]+=float((prev[f][c]-e[f][c])**2)

        mdist[f] = (mdist[f])**0.5
    
    prev=e
    totaldist = 0
    for i in range(0,len(mdist),1):
        totaldist += mdist[i]

#    print ("dist between means:",totaldist)
print("data in each cluster for k =",d,"is",classe)

for h in range(0,rows, 1):
    print(trainlabels[h],h)
