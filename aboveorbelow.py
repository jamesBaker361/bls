import csv

growth=[]
regs=[]
data=[]
indregs=[]

with open('mfpgrowthallbusiness.csv') as k:
    reader=csv.reader(k)
    for row in reader:
        growth.append(row)
        
with open('avgregsperyear.csv') as p:
    reader=csv.reader(p)
    for row in reader:
        regs.append(row)
        
with open('finaldata.csv') as y:
    reader=csv.reader(y)
    for row in reader:
        indregs.append([row[1],row[2],row[3]])

with open('mfpindustrygrowth.csv') as h:
    reader=csv.reader(h)
    for row in reader:
        f=[]
        f.append([row[1],row[2]])
        for g in growth:
            if(float(g[0])==float(row[1])):
                #print(float(g[0]),float(row[1]))
                if(float(g[3])>float(row[4])):
                    f.append('growthbelowavg')
                else:
                    f.append('growthaboveavg')
        for r in regs:
            if(float(r[0])==float(row[1])):
                for i in indregs:
                    if(float(i[0])==float(row[1])):
                        if(float(i[1])==float(row[2])):
                            if(float(i[2])>float(r[1])):
                                f.append('regaboveavg')
                            else:
                                f.append('regbelowavg')
        print(f)
        data.append(f)
with open('abovebelow.csv','w') as h:
    writer=csv.writer(h)
    writer.writerows(data)
#print(data)