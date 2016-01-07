import csv
import glob
steve=[]
countname=0

# change start frame of differetnt tracks (first track 1, 2, 3,4 enz)
starttimes=[60,150,150,150]

# change names and so on; tracknumber, gear with lvl, gear wearing lvl, name, id
data=[(1,1,0,'H. Braaksma',3623),(15,1,0,'S. Zlatanova',3641),(10,2,1,'J. Gil',3685),(20,4,4,'S. van der Spek',3611)] 

cstarttime=0
for files in glob.glob("*.csv"):
    name=str(files)
    with open(str(name)) as f:
        reader = csv.reader(f)
        count=0
        for row in reader:                
                if count>0:
                    time=0
                    starttime=count
                    id_n=str(data[cstarttime][4])
                    
                    lat=row[2]
                    lon=row[3]
                    skiptime=starttimes[cstarttime]
                    gear_withlvl=str(data[cstarttime][1])
                    name=data[cstarttime][3]                 
                    
                    toevoegen= time,starttime,id_n,lat,lon,skiptime,gear_withlvl,name
                    steve.append(toevoegen)
                    while count<(starttimes[cstarttime]+1):
                        toevoegen=list(toevoegen)
                        toevoegen[1]=count
                          
                        steve.append(toevoegen)
                        count=count+1
                elif count == 0:
                    ax=1

                count +=1
        cstarttime=cstarttime+1

steve.sort(key=lambda x: int(x[1]))

printname='test.csv'
with open(printname, 'wb') as testfile:
    csv_writer = csv.writer(testfile)
    a='time','frame','id_n','lat','lon','start_walk_frame','gear_withlvl','name'
    csv_writer.writerow(a)
    for y in steve:
        csv_writer.writerow(y)
