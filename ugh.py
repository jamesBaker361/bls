import csv
n=0
ar=0
arw=0
with open('reg2.csv','rb') as g:
    reader=csv.reader(g)
    for row in reader:
        n=n+1
        r=float(row[2])
        rw=float(row[3])
        ar=ar+r
        arw=arw+rw
        print(ar)
        print(arw)
        print(n)
avg=ar/n
avgw=arw/n
print('avg: ',avg)
print('avgw:  ',avgw)