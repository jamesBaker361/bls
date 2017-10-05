
import csv
import random

listabove=[]
listbelow=[]
aboveforty=[]
belowforty=[]

'''
with open('abovebelow.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        if(row[1]=='growthbelowavg'):
            listbelow.append(row)
        else:
            listabove.append(row)
with open('growthabove.csv','w') as v:
    writer=csv.writer(v)
    writer.writerows(listabove)
    
with open('growthbelow.csv','w')as x:
    writer=csv.writer(x)
    writer.writerows(listbelow)
'''

with open('growthabove.csv') as v:
    reader=csv.reader(v)
    for row in reader:
        listabove.append(row)

with open('growthbelow.csv') as v:
    reader=csv.reader(v)
    for row in reader:
        listbelow.append(row)
        
while(len(aboveforty)!=75):
    aboveforty.append(listabove.pop(random.randint(0,len(listabove)-1)))
    
while(len(belowforty)!=75):
    belowforty.append(listbelow.pop(random.randint(0,len(listbelow)-1)))
    
with open('aboveforty.csv','w') as l:
    writer=csv.writer(l)
    writer.writerows(aboveforty)
    
with open('belowforty.csv','w') as n:
    writer=csv.writer(n)
    writer.writerows(belowforty)