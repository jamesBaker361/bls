import csv

data=[]

with open('mfpallbusiness.csv') as d:
    reader=csv.reader(d)
    for row in reader:
        data.append([int(row[0]),float(row[1]),0.0,0.0])
        
for x in range(1,len(data)):
    data[x][2]=data[x][1]-data[x-1][1]
    data[x][3]=(data[x][1]/data[x-1][1])-1.0
print(data)

with open('mfpgrowthallbusiness.csv','w') as b:
    writer = csv.writer(b)
    writer.writerows(data)