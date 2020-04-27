#!/bin/env python
import sys
import math
import random



class ML_lib:
  
    def classes(self, dataset, labelc):
        return list(set(row[labelc] for row in dataset))
    
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
    
    def read_label(self):
        labelfile   = sys.argv[2]
        f           = open(labelfile)
        trainlabels = {}
        l           = f.readline()
        while (l != ''):
            a                      = l.split()
            trainlabels[int(a[1])] = int(a[0])
            l                      = f.readline()
        return trainlabels

    def split(self, thr, cols, data_set):
        left  = []
        right = []
    
        for r in data_set:
            if r[cols] < thr:
                left.append(r)
            else:
                right.append(r)
        return left, right  
            
    def gini_index(self, groups, classes):
        left  = groups[0]
        right = groups[1]
    
        tot_rows = len(left) + len(right)
        gini     = 0.0
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            prob = 1
            for class_val in classes:
                p    = [row[-1] for row in group].count(class_val) / size
                prob = prob * p
            gini += (prob) * (size / tot_rows)
        return gini
    
    def marge_data_label(self, data, label):
#        pred = []
#        test_data = []
        diff_data = {"pred": [], "data": data, "data_set": [], "test_data": []}
        for r in range(len(diff_data["data"])):
            if (label.get(r) != None):
                diff_data["data"][r].append(label[r])
            else:
                diff_data["pred"].append(data[r])
            diff_data["test_data"].append(data[r])
#        data_set = []
        for r in diff_data["data"]:
            length = len(r)
            if length == len(diff_data["data"][0]):
                diff_data["data_set"].append(r)
        return diff_data
    
    def get_split(self, data_set, labelc):
        classval = self.classes(data_set, labelc)
        stump    = { 'column': 0, 'row': 0, 'value': 0, 'gini': 1, 'groups': None, 'sim_count': 0}
        for col in range(len(data_set[0]) - 1):
            for r in range(len(data_set)):
                grps = self.split(data_set[r][col], col, data_set)
                gini_temp = self.gini_index(grps, classval)
                if (gini_temp < stump['gini']):
                    stump['column']   = col
                    stump['row']      = r
                    stump['value']    = data_set[r][col]
                    stump['gini']     = gini_temp
                    stump['groups']   = grps
                elif gini_temp == stump['gini']:
                    stump['sim_count'] = stump['sim_count'] + 1
    
        if (stump['sim_count'] == ((len(data_set) * 2) - 1)):
            stump['column'] = 0
            b_rowVal = data_set[0][stump['column']]
            stump['row'] = 0
            for r in range(len(data_set)):
                if data_set[r][stump['column']] > b_rowVal:
                    stump['row'] = r
                    b_rowVal     = data_set[r][stump['column']]
            stump['value']  = data_set[stump['row']][stump['column']]
            stump['gini']   = gini_temp
            stump['groups'] = self.split(data_set[stump['row']][stump['column']], stump['column'], data_set)
    
        return stump
    
    def Split_Line(self, new_cols, new_value, data_set):
        win_col = list()
        maxNum = -9999
        for r in range(len(data_set)):
            win_col.append(data_set[r][new_cols])
        win_col.sort()
        for r in range(len(data_set)):
            val = data_set[r][new_cols]
            if val < new_value:
                if val > maxNum:
                    maxNum = val

        s = (maxNum + new_value) / 2
        return s
    
    def ClassSide(self, column, value, labelColb, temp_data):
        class_val = self.classes(temp_data, labelColb)
        if (len(class_val) == 1):
            if (class_val[0] == 1):
                class_val.append(0)
            else:
                class_val.append(1)
        class_val.sort()
        
        sideA = 0
        sideB = 0
        sides = {"lest": None, "right": None}
        for a in range(0, len(temp_data)):
            if (temp_data[a][column] < value):
                if (temp_data[a][labelColb] == class_val[0]):
                    sideA = sideA + 1
                else:
                    sideB = sideB + 1
            if (sideA > sideB):
                sides["left"] = class_val[0]
                sides["right"] = class_val[1]
            else:
                sides["left"] = class_val[1]
                sides["right"] = class_val[0]

        return sides
    
    def Stump_predict(self, column, value, test_data_point, sides):

        classification = 0
        for row in [test_data_point]:
            if row[column] < value:
                classification = sides["left"]

            else:
                classification = sides["right"]

        return classification
            
    
    def bagging(self, diff_data, labelc):
        data_cols     = len(diff_data["data_set"][0]) - 1
        data_rows     = len(diff_data["data_set"])
        ratio         = 1/3
        numBootColumn = round((data_cols + 1) * ratio)
        class_val     = self.classes(diff_data["data_set"], labelc)
        class_val.sort()
        
        for test_point in range(len(diff_data["test_data"])):
            col1 = 0
            col2 = 0
            
            for k in range(0, 100):
                random_col = random.sample(range(0, data_cols), data_cols)
                random_col.append(labelc)
            
                random_row = []
                for row in range(data_rows):
                    random_row.append(random.randint(0, data_rows - 1))
     
                temp_data = [0] * len(random_row)
                temp = [0] * len(random_col)
                i = 0
                j = 0
                for r in random_row:
                    for c in random_col:
                        temp[i] = diff_data["data_set"][r][c]
                        i       = i + 1
                    temp_data[j] = temp
                    temp         = [0] * len(random_col)
                    i            = 0
                    j            = j + 1
                labelColb   = len(temp_data[0]) - 1
                stump       = self.get_split(temp_data, labelColb)
                
                sides       = self.ClassSide(stump['column'], stump['value'], labelColb, temp_data)

                best_column = stump['column']
                b_col_data  = random_col[best_column]
                predict     = self.Stump_predict(b_col_data, stump['value'], diff_data["test_data"][test_point], sides)


                if predict == class_val[0]:
                    col1 += 1
                else:
                    col2 += 1
            
            if col1 > col2:
                print(str(class_val[0]))
            else:
                print(str(class_val[1]))

def main():
    ML_lib_obj = ML_lib()
    
    data                = ML_lib_obj.read_data()
    label               = ML_lib_obj.read_label() 
#    cols                = len(data[0])
#    rows                = len(data)
    diff_data           = ML_lib_obj.marge_data_label(data, label)
    labelc              = len(diff_data["data_set"][0]) - 1
#    stump               = ML_lib_obj.get_split(diff_data["data_set"], labelc)
#    s                   = ML_lib_obj.Split_Line(stump['column'], stump['value'], diff_data["data_set"])
    ML_lib_obj.bagging(diff_data, labelc)

if __name__ == "__main__":
    main()


