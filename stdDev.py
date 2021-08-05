import csv
import math

with open("data.csv", newline="") as f:
    read=csv.reader(f)
    fileData = list(read)

data = fileData.pop(0)

def mean(data):
    n=len(data)
    total = 0
    for x in data:
        total +=int(x)

    mean = total/n
    return(mean)

squaredList =[]
for number in data:
    a = int(number) - mean(data)

    a = a**2

    squaredList.append(a)

sum=0

for i in squaredList:
    sum = sum + i

result = sum/(len(data)-1)

#getting the standard deviation
standardDev = math.sqrt(result)

print("Standard Deviation: " +str(standardDev))