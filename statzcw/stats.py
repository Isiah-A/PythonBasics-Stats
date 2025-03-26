import math
from typing import List

def zcount(data: List[float]) -> float :
    count = len(data)
    return count

def zmean(data: List[float]) -> float :
    avg = sum(data) / len(data)
    return avg

def zmode(data: List[float]) -> float :
    return max(set(data), key=data.count)

def zmedian(data: List[float]) -> float :
    d = len(data) #need length of list
    data.sort() #sort list in order first
    if d % 2 == 0:
        median1 = data[d // 2]
        median2 = data[d // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median  = data[d // 2]
    return median

def zvariance(data: List[float]) -> float :
    avg = sum(data) / len(data)
    formula = sum((i - avg) ** 2 for i in data) / len(data)
    return formula
	
def zstddev(data: List[float]) -> float :
    avg = sum(data) / len(data)
    variance = sum(pow(x - avg, 2) for x in data) / len(data)
    sqrt = math.sqrt(variance)
    return sqrt


def zstderr(data: List[float]) -> float :
    avg = sum(data) / len(data)
    variance = sum(pow(x - avg, 2) for x in data) / len(data)
    stderr = variance ** 0.5
    return stderr

def cov(a, b):
    avg1 = a.sum() / len(b)
    avg2 = b.sum() / len(a)
    return sum([(x - avg1) * (y - avg2) for x, y in zip(a,b)]) / (len(a) - 1)

def zcorr(datax: List[float], datay: List[float]) -> float :
    avg1 = sum(datax) / len(datax)
    variance1 = sum(pow(x - avg1, 2) for x in datax) / len(datax)
    datax_dev = math.sqrt(variance1)

    #calc mean and deviation of both lists...

    avg2 = sum(datay) / len(datay)
    variance2 = sum(pow(x - avg2, 2) for x in datay) / len(datay)
    datay_dev = math.sqrt(variance2)

    corr_numerator = 0.0
    for i in range(len(datax)):
        corr_numerator += ((datax[i] - avg1) * (datay[i] - avg2))
    corr_denominator = datax_dev * datay_dev

    corr = corr_numerator / corr_denominator
    return corr



def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
