import csv
import numpy as np
reader = csv.DictReader(file("train.csv", 'rb'))

cont = list(reader)

print len(cont)
print cont[0]

np.random.seed(1002)
np.random.shuffle(cont)

data = []


for col in cont:
    s = ''
    y = col["Score"]
    s += y 
    s += " "
    for i in range(1,33):
        key = "Col_" + str(i)
        if col[key].isdigit():
            tmp = str(i-1) + ":" + col[key] + " "
        else:
            tmp = str(i-1) + ":" + str(ord(col[key]) - ord('a') ) + " "
        s += tmp
    data.append(s)

fwtrain = open("train.txt", 'w')
fwvalid = open('valid.txt', 'w')

for i in data[:28000]:
    fwtrain.write(i + '\n')
for i in data[28001:]:
    fwvalid.write(i + '\n')
fwtrain.close()
fwvalid.close()

    
