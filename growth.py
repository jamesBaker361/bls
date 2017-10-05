import csv

#the new file will have format mfp,year,industrycode,Industry-relevant restriction count (Industry Regulation Index),Industry-relevant words, net change in mfp since last year, and percentage change in mfp since last year

data=[]
n=0

for x in range(50):
    data.append([str(1970+x),float(0),float(0)])
    
with open('reg2.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        for a in data:
            if(a[0]==row[0]):
                #a.append([row[2],row[3]])
                a[1]=a[1]+float(row[2])
                a[2]=a[2]+float(row[3])
                #print(a)
                break
        if(row[0]=='2009'):
            n=n+1

for d in data:
    d[1]=d[1]/n
    d[2]=d[2]/n

print(data)
with open('avgregsperyear.csv','w') as h:
    writer=csv.writer(h)
    print(writer)
    writer.writerows(data)