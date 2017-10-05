import csv
import string

datamfp=[]
datareg=[]
databoth=[]
        
#year,industry,Industry-relevant restriction count (Industry Regulation Index),Industry-relevant words- reg.csv 
#indusrty, ,Year,Period,Label,Value -bettermfpindustrys.csv
with open('bettermfpindustrys.csv','rb') as z:
    reader=csv.reader(z)
    for row in reader:
        datamfp.append(row)
        
with open('reg.csv','rb') as h:
    reader =csv.reader(h)
    for row in reader:
        datareg.append(row)

for regrow in datareg:
    for mfprow in datamfp:
        if(mfprow[0] == regrow[1]):
            if(mfprow[1] == regrow[0]):
                u=mfprow+regrow
                del u[0:4]
                databoth.append(u)

                
with open('finaldata.csv','w') as k:
    writer=csv.writer(k)
    writer.writerow(['mfp','year','industrycode','Industry-relevant restriction count (Industry Regulation Index)','Industry-relevant words- reg.csv'])
    writer.writerows(databoth)