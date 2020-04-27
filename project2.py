import sys
import math
import random
import array
import copy
import numpy as np

from sklearn import svm
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors.nearest_centroid import NearestCentroid
from tqdm import tqdm


class file_handling:
    def read_data():
        datafile = sys.argv[1]
        data = []
        with open(datafile, 'r') as datafile:
            for r in datafile:
                a = r.split()
                l = array.array("i")            
                for i in a:
                  l.append(int(i))
                data.append(l)
        return data
    
    def read_label():
         labelfile = sys.argv[2]
         train_labels = array.array("i")
         with open(labelfile, "r") as label_file:
             for r in label_file:
                 a = r.split()
                 train_labels.append(int(a[0]))
         return train_labels

class ML_models:
    def Pearson_Correlation(self, x, y,fi):
        self.x = x
        self.y = y
        self.fi= fi
        sumX  = 0.1
        sumX2 = 0.1
        switch    = 0
        rows      = len(x)
        cols      = len(x[0])
        pc = array.array("f")
        for i in tqdm(range(0, int(.4*cols), 1)):
            switch += 1
            sumY    = 0.1
            sumY2   = 0.1
            sumXY   = 0.1
            for j in range(0, rows, 1):
                if(switch == 1):
                    sumX  += y[j]
                    sumX2 += y[j] ** 2
                sumY += x[j][i]
                sumY2 += x[j][i] ** 2
                sumXY += y[j] * x[j][i]
            temp = ((rows * sumXY - sumX * sumY)) / (((rows * sumX2 - (sumX ** 2)) * (rows * sumY2 - (sumY ** 2))) ** (0.5))
        pc.append(abs(temp))
        
        save_array = array.array("f")
        my_feature = array.array("i")
        for i in tqdm(range(0, fi, 1)):
            selected_feature = max(pc)
            save_array.append(selected_feature)
            feature_index = pc.index(selected_feature)
            pc[feature_index] = -1
            my_feature.append(feature_index)
        return my_feature
      
def main():
    file_handling_obj = file_handling()
    ML_models_obj     = ML_models()
    data = file_handling.read_data()
    train_labels = file_handling.read_label()
    rows, cols, rowsl = len(data), len(data[0]), len(train_labels)
    train_labels = file_handling.read_label()
    print("Feature Selection started")
    neededFea = ML_models_obj.Pearson_Correlation(data, train_labels, 2000)
    print("Done with feature selection", end="")
    print(neededFea)
    #clf_svm = svm.SVC(gamma = 0.001)
    #a = clf_svm.fit(data, train_labels[0])
    #print(a)
 
       
if __name__ == "__main__":
    main()


