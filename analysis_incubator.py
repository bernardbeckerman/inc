import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import code
pd.set_option('display.precision',10)

def getTime(tstr):
    m2s = 60
    h2s = 3600
    tsplit = tstr.split()
    hms = list(map(int,tsplit[1].split(':')))
    if (hms[0]==12):
        hms[0] = 0
    if (tsplit[2]=='PM'):
        hms[0] += 12
    time = hms[0]*h2s + hms[1]*m2s + hms[2]
    return time

def isViol(fbistr):
    fbi_viol = ['01A','02','03','04A','04B']
    if fbistr in fbi_viol:
        return True
    else:
        return False

def isIndx(fbistr):
    fbi_indx = ['01A','02','03','04A','04B','05','06','07','09']
    if fbistr in fbi_indx:
        return True
    else:
        return False

def isProp(fbistr):
    fbi_prop = ['05','06','07','09']
    if fbistr in fbi_prop:
        return True
    else:
        return False

def getHist(ax):
    n,bins = [],[]
    for rect in ax.patches:
        ((x0, y0), (x1, y1)) = rect.get_bbox().get_points()
        n.append(y1-y0)
        bins.append(x0) # left edge of each bin
    bins.append(x1) # also get right edge of last bin
    return n,bins

#columns
date = 'Date'
fbi  = 'FBI Code'
iucr = 'IUCR'
ptyp = 'Primary Type'
desc = 'Description'
locd = 'Location Description'
arr  = 'Arrest'
dom  = 'Domestic'
ward = 'Ward'
id   = 'ID'
cnum = 'Case Number'
blok = 'Block'
comm = 'Community Area'
xcrd = 'X Coordinate'
ycrd = 'Y Coordinate'
year = 'Year'
updt = 'Updated On'
lat  = 'Latitude'
lon  = 'Longitude'
lct  = 'Location'
tims = 'Time in Seconds'
timh = 'Time in Hours'
viol = 'Violent'
indx = 'Indexed'
prop = 'Property'

fbi_indx  = ['01A','02','03','04A','04B','05','06','07','09']
fbi_nindx = ['01B','08A','08B','10','11','12','13','14','15','16','17','18','19','20','22','24','26']
fbi_viol  = ['01A','02','03','04A','04B']
fbi_nviol = ['01B','05','06','07','08A','08B','09','10','11','12','13','14','15','16','17','18','19','20','22','24','26']
fbi_prop  = ['05','06','07','09']

#load data
a = pd.read_csv('Crimes_-_2001_to_present.csv', nrows=1000000)
a[tims] = a[date].apply(getTime)
a[viol] = a[fbi].apply(isViol)
a[timh] = a[tims].apply(lambda x: int(x/3600.0))

gviol   = a.groupby(viol)
lines   = gviol[timh].hist(alpha=0.4,bins=24,range=[0,24],normed=True)
n,bins  = getHist(lines[0])
n_viol  = n[0:24]
n_nviol = n[24:48]
b_viol  = bins[0:24]
b_nviol = bins[24:48]

gvy = gviol.get_group(True)
gvn = gviol.get_group(False)

#print probability of arrest for violent and nonviolent crimes by hour
print (gvy.groupby(timh)['Arrest'].mean())
print (gvn.groupby(timh)['Arrest'].mean())

#print frequency of violent/nonviolent crime vs. hour of day
for i in range(24):
    print (str(i) + " " + str(n_viol[i]) + " " + str(n_nviol[i]))
