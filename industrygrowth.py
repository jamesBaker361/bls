import csv

#we got 30 industries
#we got 26 years

data=[]

yearminus=0.0

with open('finaldata.csv') as j:
    reader=csv.reader(j)
    for row in reader:
        data.append([row[0],row[1],row[2]])

for d in data:
    if (d[1] != '1990'):
        yearminus=(int(d[1])-1)
        #print(yearminus)
        for z in data:
            #if ((int(z[1])==yearminus)&&(z[2]==d[2])):
            if(int(z[1])==yearminus):
                if(z[2]==d[2]):
                    d.append(float(d[0])-float(z[0]))
                    d.append((float(d[0])/float(z[0]))-1.0)
print(data)

with open('mfpindustrygrowth.csv','w') as w:
    writer=csv.writer(w)
    writer.writerows(data)