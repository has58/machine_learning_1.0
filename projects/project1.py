import sys
import math


class file_handling:
    '''
    def __inti__(self):
        self.read_data()
        self.read_label()
    '''    
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
        print("************** HELLO WORLD*********************")
        return data
    
    def read_label(self):
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
        print("************** HELLO WORLD*********************")
        return trainlabels
         
        
def main():
    file_handling_obj = file_handling()
    file_handling_obj.read_data()
    file_headling_obj.read_label()
if __name__ == "__main__":
    main()


