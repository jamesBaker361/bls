import csv

def countbelow(data):
    count=0
    for d in data:
        if(d[2]=='regbelowavg'):
            count=count+1
    return(count)

with open('belowforty.csv') as x:
    reader=csv.reader(x)
    print(countbelow(reader))
    
with open('aboveforty.csv') as x:
    reader=csv.reader(x)
    print(countbelow(reader))