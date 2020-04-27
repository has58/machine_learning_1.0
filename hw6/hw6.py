import sys
import math



class file_handling:
  
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
        pred = []
        for r in range(len(data)):
            if (label.get(r) != None):
                data[r].append(label[r])
            else:
                pred.append(data[r])
        data_set = []
        for r in data:
            length = len(r)
            if length == len(data[0]):
                data_set.append(r)
        return pred, data, data_set
    
    def get_split(self, data_set, labelc):
        classval = self.classes(data_set, labelc)
        print(classval)
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
            stump['groups'] = split(data_set[stump['row']][stump['column']], stump['column'], data_set)
    
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

                
         
        
def main():
    file_handling_obj = file_handling()
    
    data                    = file_handling_obj.read_data()
    label                   = file_handling_obj.read_label()   
    cols                    = len(data[0])
    rows                    = len(data)
    pred, data, data_set    = file_handling_obj.marge_data_label(data, label)
    labelc                  = len(data_set[0]) - 1
    stump                   = file_handling_obj.get_split(data_set, labelc)
    s                       = file_handling_obj.Split_Line(stump['column'], stump['value'], data_set)
    print('Best column:', stump['column'])
    print('Split point value:', s)     

if __name__ == "__main__":
    main()


