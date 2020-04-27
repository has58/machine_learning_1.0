#!/bin/env python
import sys
import math
import random



class ML_lib:
     
    def read_data(self):
        datafile = sys.argv[1]
        f        = open(datafile, 'r')
        data     = []
        l        = f.readline()
        
        while (l != ''):
            a   = l.split()
            l2  = []
            for j in range(0, len(a), 1):
                l2.append(float(a[j]))
            l2.append(float(1))
            data.append(l2)
            l = f.readline()
        f.close()
        return data
    def clusting(self, data):
        cols = len(data[0])
        rows = len(data)
        clus_num  = int(sys.argv[2])
        col = [0 for _ in range(0, cols, 1)]
        temp = [col for _ in range(0, clus_num, 1)]
        
        for i in range(0, clus_num, 1):
            rand_val1 = random.randrange(1, rows - 1)
            temp[i] = data[rand_val1]
        
        trainlabels = {}
        n = [0.1 for _ in range(0, clus_num, 1)]
        distances = [0.1 for _ in range(0, clus_num, 1)]
        prev = [[0]*cols for i in range(clus_num)]
        mdist = [0 for _ in range(0, clus_num, 1)]
        
        total_distances = 1
        classes = []
        while (total_distances > 0):
            for i in range(0, rows, 1):
                distances = []
                
                for j in range(0, clus_num, 1):
                    distances.append(0)

                for j in range(0, clus_num, 1):
                    for k in range(0, cols, 1):
                        distances[j] += ((data[i][k] - temp[j][k])**2)

                for j in range(0, clus_num, 1):
                    distances[j] = (distances[j])**0.5

                mindist=0
                mindist = min(distances)
                for j in range(0, clus_num, 1):
                  if(distances[j]==mindist):
                      trainlabels[i] = j
                      n[j]+=1
                      break

            temp = [[0]*cols for g in range(clus_num)]
            col = []
            
            for i in range(0, rows, 1):
                for j in range(0, clus_num, 1):
                    if(trainlabels.get(i) == j):
                        for k in range(0, cols, 1):
                            temp1 =  temp[j][k]
                            temp2 =  data[i][k]
                            temp[j][k] = temp1 + temp2
            for k in range(0, cols, 1):
                for i in range(0, clus_num, 1):
                    temp[i][k] = temp[i][k]/n[i]

            classes = [int(g) for g in n]
            n=[0.1]*clus_num
            
            mdist = []
            for j in range(0, clus_num, 1):
                mdist.append(0)
            for j in range(0, clus_num, 1):
                for k in range(0, cols, 1):
                    mdist[j]+=float((prev[j][k]-temp[j][k])**2)

                mdist[j] = (mdist[j])**0.5
            
            prev=temp
            total_distances = 0
            for i in range(0,len(mdist),1):
                total_distances += mdist[i]
        for i in range(0,rows, 1):
            print(trainlabels[i],i)

def main():
    ML_lib_obj = ML_lib()
    
    data       = ML_lib_obj.read_data()
    ML_lib_obj.clusting(data)

if __name__ == "__main__":
    main()


