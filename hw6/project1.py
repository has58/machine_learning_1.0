import sys
import math



class file_handling:
  
    def classes(dataset, labelc):
        return list(set(row[labelc] for row in dataset))
    
    def read_data(self):
        datafile = sys.argv[1]
        f = open(datafile, 'r')
        data = []
        l = f.readline()
        
        while (l != ''):
            a = l.split()
            l2 = []
            for j in range(0, len(a), 1):
                l2.append(float(a[j]))
            l2.append(float(1))
            data.append(l2)
            l = f.readline()
        f.close()
        return data
    
    def read_label(self):
        labelfile = sys.argv[2]
        f = open(labelfile)
        trainlabels = {}
        l = f.readline()
        while (l != ''):
            a = l.split()
            trainlabels[int(a[1])] = int(a[0])
            l = f.readline()
        return trainlabels

    def split(thr, cols, dat_set):
        left = []
        right = []
    
        for r in data_set:
            if r[cols] < thr:
                left.append(r)
            else:
                right.append(r)
        return left, right  
            
    def gini_index(groups, classes):
        left = groups[0]
        right = groups[1]
    
        tot_rows = len(left) + len(right)
        gini = 0.0
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            prob = 1
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                prob = prob * p
            gini += (prob) * (size / tot_rows)
        return gini\
    
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
    
    def get_split(data_set, labelc):
        classval = classes(data_set, labelc)
        stump = { 'new_cols': 0, 'new_row': 0, 'new_value': 0, 'new_gini': 1, 'new_grp': None, 'sim_count': 0}
        for col in range(len(data_set[0]) - 1):
            for row in range(len(data_set)):
                grps = split(data_set[row][col], col, data_set)
                gini = gini_index(grps, classval)
                if gini < stump[new_gini]:
                    stump[new_cols]   = col
                    stump[new_row]   = row
                    stump[new_value] = data_set[row][col]
                    stump[new_gini]  = gini
                    stump[new_grp]   = grps
                elif gini == stump[new_gini]:
                    sim_count = sim_count + 1
    
        if (sim_count == ((len(data_set) * 2) - 1)):
            stump[new_cols] = 0
            b_rowVal = data_set[0][stump[new_cols]]
            stump[new_row] = 0
            for row in range(len(data_set)):
                if data_set[row][stump[new_cols]] > b_rowVal:
                    stump[new_row] = row
                    b_rowVal = data_set[row][stump[new_cols]]
            stump[new_value] = data_set[stump[new_row]][stump[new_cols]]
            stump[new_gini] = gini
            stump[new_grps] = split(data_set[stump[new_row]][stump[new_cols]], stump[new_cols], data_set)
    
        return {'column': b_coln, 'row': b_row, 'value': b_value, 'groups': b_groups, 'gini': b_gini}

                
         
        
def main():
    file_handling_obj = file_handling()
    
    data                    = file_handling_obj.read_data()
    label                   = file_handling_obj.read_label()   
    cols                    = len(data[0])
    rows                    = len(data)
    pred, data, data_set    = file_handling_obj.marge_data_label(data, label)

         

if __name__ == "__main__":
    main()


