import copy
import sys
import math
import random
import array
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
    
    def extract_Column(self, arg_matrix, i):
        return [[row[i]] for row in arg_matrix]

    def merge_Column(self, a, b):
        return [x + y for x, y in zip(a, b)]
    
    def CreateDataSet(self, fea, dat):
        newData = self.extract_Column(dat, fea[0])
        fea.remove(fea[0])
        length = len(fea)
        for i in range(0, length, 1):
            temp = self.extract_Column(dat, fea[0])
            newData = self.merge_Column(newData, temp)
            fea.remove(fea[0])
        return newData

class ML_models:
    def mean(self, xm, ym):
        self.xm = xm
        self.ym = ym
        meanx = 0.01
        for i in xm:
        	  meanx += i 
        meany = 0.01
        for i in ym:
            meany += i
        return (meanx/len(xm)), (meany/len(ym))
       
    def standard_deviation(self, xs, ys):
        self.xs = xs
        self.ys = ys
        sdx = 0
        sdy = 0
        mx, my = self.mean(xs, ys)
        for i in xs:
       	    sdx += (i - mx)**2
       	for i in ys:
            sdy += (i - my)**2
       	sdx = (sdx/(len(xs)-1))**(0.5)
        sdy = (sdy/(len(ys)-1))**(0.5)
        return sdx, sdy
    '''
    def Pearsion_Correlation(self, x, y, fi):
        self.x  = x
        self.y  = y
        self.fi = fi
        rows    = len(x)
        cols    = len(x[0])
        cov = 0
        for i in 
    '''
       
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
    feat = 10
    rows, cols, rowsl = len(data), len(data[0]), len(train_labels)
    train_labels = file_handling.read_label()
    print("Feature Selection started")
    TEMP = ML_models_obj.Pearson_Correlation(data, train_labels, 2000)
    print("Done with feature selection", end="\n")
    savedFea = copy.deepcopy(TEMP)
    data1 = file_handling_obj.CreateDataSet(TEMP, data)
    clf_svm = svm.SVC(gamma=0.001)
    accuracy = 0
    feature = []
    iterations = 5
    for i in range(iterations):

        print(i)
        rowIDs = []
        for i in range(0, len(data), 1):
                rowIDs.append(i)
        
        random.shuffle(rowIDs)
    
        trainX, trainY = [], []
        validX, validY = [], []
        
        for i in range(0, int(.9*len(rowIDs)), 1):
                idx = rowIDs[i]
                trainX.append(data1[idx])
                trainY.append(train_labels[idx])
        for i in range(int(.9*len(rowIDs)), len(rowIDs), 1):
                idx = rowIDs[i]
                validX.append(data1[idx])
                validY.append(train_labels[idx])
        
        newRows = len(trainX)
        newCols = len(trainX[0])
        newRowst = len(validX)
        newColst = len(validX[0])
        newRowsL = len(trainY)
    
        Pear_Features = ML_models_obj.Pearson_Correlation(trainX, trainY, feat)
    
        feature.append(Pear_Features)
        argument = copy.deepcopy(Pear_Features)
    
        data_fea = file_handling_obj.CreateDataSet(argument, trainX)
    
        clf_svm.fit(data_fea, trainY)

    
        TestFeatures = ML_Models_obj.Pearson_Correlation(validX, validY, feat)
    
        test_fea = file_handling_obj.CreateDataSet(TestFeatures, validX)
    
        len_test_fea = len(test_fea)
        counter_svm = 0
        my_counter = 0
        
        for j in range(0, len_test_fea, 1):
            predLab_svm = int(clf_svm.predict([test_fea[j]]))
            
    
    
        accuracy_svm += counter_svm / len_test_fea
   
        my_accuracy += my_counter / len_test_fea
    
    print("\nFeatures: ", feat)
    
    originalFea = array.array("i")
    for i in range(0, feat, 1):
        realIndex = savedFea[best_Features[i]]
        originalFea.append(realIndex)
    
    print("The features are: ", originalFea)
    feature_file = open("features", "w+")
    for i in range(0, len(originalFea), 1):
        feature_file.write(str(originalFea[i]) + "\n")
    
    # Calculate Accuracy
    argument1 = copy.deepcopy(originalFea)
    Acc_Data = CreateDataSet(argument1, data)
    
    clf_svm.fit(Acc_Data, train_labels)
    
    svm_counter = 0
    LeCounter = 0
    k = len(Acc_Data)
    for i in range(0, k, 1):
        predLab_svm = int(clf_svm.predict([Acc_Data[i]]))
        if (predLab_svm == train_labels[i]):
            svm_counter += 1
    
    FinalAcc = LeCounter / k
    SVMAc = svm_counter / k
    print("Accuracy: ", FinalAcc * 100)
    
    # Read Test data
    test_file = sys.argv[3]
    test_data = []
    with open(test_file, "r") as teat_file:
        for line in test_file:
            temp = line.split()
            l = array.array("i")
            for i in temp:
                l.append(int(i))
            test_data.append(l)
    
    argument2 = copy.deepcopy(originalFea)
    test_data1 = CreateDataSet(argument2, test_data)
    
    # create a 
    
    print("\nPredicted labels of the test data are saved in testLabels file")
    print("Done everything")
    
    
       
if __name__ == "__main__":
    main()


