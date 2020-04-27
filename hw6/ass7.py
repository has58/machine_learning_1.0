import sys
import random


def classes(dataset, labelCol):
    return list(set(row[labelCol] for row in dataset))


def testSplit(threshold, column, dataset):
    left = list()
    right = list()

    for row in dataset:
        if row[column] < threshold:
            left.append(row)
        else:
            right.append(row)
    return left, right


def ginindex(g, classes):
    left = g[0]
    right = g[1]

    tot_rows = len(left) + len(right)
    gini = 0.0
    for g1 in g:
        size = len(g1)
        # print("Group is ", str(g1))
        if size == 0:
            continue
        probability = 1
        for class_val in classes:
            p = [row[-1] for row in g1].count(class_val) / size
            probability = probability * p
        gini += (probability) * (size / tot_rows)
    return gini


def get_split(dataset, labelColumn):
    classval = classes(dataset, labelColumn)
    bcolumn1 = 0
    brw1 = 0
    bvl1 = 0
    bg12n1 = 1
    bg12 = None
    sim_count = 0
    for col in range(len(dataset[0]) - 1):
        for row in range(len(dataset)):
            g = testSplit(dataset[row][col], col, dataset)
            gini = ginindex(g, classval)

            if gini < bg12n1:
                bcolumn1 = col
                brw1 = row
                bvl1 = dataset[row][col]
                bg12n1 = gini
                bg12 = g
            elif gini == bg12n1:
                sim_count = sim_count + 1

    if (sim_count == ((len(dataset) * 2) - 1)):
        bcolumn1 = 0
        brw1Val = dataset[0][bcolumn1]
        brw1 = 0
        for row in range(len(dataset)):
            if dataset[row][bcolumn1] > brw1Val:
                brw1 = row
                brw1Val = dataset[row][bcolumn1]
        bvl1 = dataset[brw1][bcolumn1]
        bg12n1 = gini
        bg12 = testSplit(dataset[brw1][bcolumn1], bcolumn1, dataset)

    return {'column': bcolumn1, 'row': brw1, 'value': bvl1, 'groups': bg12}


def getSplitLine(bcolumn1, bvl1, dataset):
    win_col = list()
    maxNumber = -9999  
    for a in range(len(dataset)):
        win_col.append(dataset[r][bcolumn1])
    win_col.sort()
    for a in range(len(dataset)):
        val = dataset[a][bcolumn1]
        if val < bvl1:
            if val > maxNumber:
                maxNumber = val

    z = (maxNumber + bvl1) / 2
    return z


def ClassSide(b_col, b_split, labelColumn, dataset):
    classval = classes(dataset, labelColumn)
    if (len(classval) == 1):
        if (classval[0] == 1):
            classval.append(0)
        else:
            classval.append(1)
    classval.sort()

    sideA = 0
    sideB = 0
    for a in range(0, len(dataset)):
        if (dataset[a][b_col] < b_split):
            if (dataset[a][labelColumn] == classval[0]):
                sideA = sideA + 1
            else:
                sideB = sideB + 1
        if (sideA > sideB):
            left = classval[0]
            right = classval[1]
        else:
            left = classval[1]
            right = classval[0]

    return {'left': left, 'right': right}


def Stump_predict(Bcol, Bsplit, newValue, leftClass, rightClass):

    classification = 0
    for row in [newValue]:
        if row[Bcol] < Bsplit:
            classification = leftClass

        else:
            classification = rightClass

    return classification


datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
i = 0
l = f.readline()
while (l != ''):
    x = l.split()
    l2 = []
    for j in range(0, len(x), 1):
        l2.append(float(x[j]))
    data.append(l2)
    l = f.readline()
print("****** DATA *******", data)
tdatafile = sys.argv[2]
t = open(tdatafile, 'r')
label = {}
l = t.readline()
while (l != ''):
    x = l.split()
    label[int(x[1])] = int(x[0])
    l = t.readline()

test = list()

for a in range(len(data)):
    if (label.get(a) != None):
        data[a].append(label[a])
    test.append(data[a])
print("****** TEST *******", test)
dataset = list()
for a in data:
    length = len(a)
    if length == len(data[0]):
        dataset.append(a)


ncolumns = len(dataset[0]) - 1
nrows = len(dataset)
labelColumn = len(dataset[0]) - 1
ratio = 1 / 3
numBootColumn = round((ncolumns + 1) * ratio)
classval = classes(dataset, labelColumn)
classval.sort()

for test_pt in range(len(test)):
    c1 = 0
    c2 = 0

    for k in range(0, 100):
        ranCol = random.sample(range(0, ncolumns), ncolumns)
        ranCol.append(labelColumn)

        ranRow = list()
        for row in range(nrows):
            ranRow.append(random.randint(0, nrows - 1))


        b_data = [0] * len(ranRow)
        temp = [0] * len(ranCol)
        i = 0
        j = 0
        for r in ranRow:
            for c in ranCol:
                temp[i] = dataset[r][c]
                i = i + 1
            b_data[j] = temp
            temp = [0] * len(ranCol)
            i = 0
            j = j + 1

        labelColb = len(b_data[0]) - 1
        stump = get_split(b_data, labelColb)

        cs = ClassSide(stump['column'], stump['value'], labelColb, b_data)


        best_column = stump['column']
        b_column_data = ranCol[best_column]
        predict = Stump_predict(b_column_data, stump['value'], test[test_pt], cs['left'], cs['right'])


        if predict == classval[0]:
            c1 += 1
        else:
            c2 += 1

    if c1 > c2:
        final_predict = classval[0]
        print('Final prediction', str(test[test_pt]), ':', str(final_predict))
    else:
        final_predict = classval[1]
        print('Final prediction', str(test[test_pt]), ':', str(final_predict))

