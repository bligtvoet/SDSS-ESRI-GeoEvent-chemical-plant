import csv
import random
import uuid

def csvreaderwriter(filename_1):
    
    """ only tested for Garmin Oregeon 650
    variable 1: csv file with info from basecamp table.
        how:    open the table of a track and copy all field in the table to exel.
                In exel save as comma seperated value (not windows csv)
    variable 2: csv file exported from basecamp.
        how:    in basecamp select tract. Got to file-export-save as csv
    
    """


    with open(filename_1,'r') as csv_file:
        reader=csv.reader(csv_file)
        new_file=open('Sensors_rpress_2.csv', 'wb')
        writer= csv.writer(new_file, delimiter=',')
        writer.writerow(['time','id','longitude','lattitude','diameter','pressure','normal_pressure','is_online','on_pipe','coords'])
        
        rowlist=[]
        count=0
        idfield=0
        
        for row in reader:
            try:
                popper=row.pop(2)
                formatting=float(popper)
                row.insert(2,formatting)
                row.insert(0,count)
                row.insert(1,idfield)
                row.append(28992)
                rowlist.append(row)
            except ValueError:
                continue

        
        

        for times in range(65):             # number of changes per point
            print times

            count=0
            for each in rowlist:
                each.pop(5)
                new_pressure=int(random.gauss(100, 5))
                each.insert(5,new_pressure)
                
                each.pop(0)
                each.insert(0,times)

                each.pop(1)
                each.insert(1,count)
                
                writer.writerow(each)
                count+=1
                
        new_file.close
        
    print 'finished'
        




csvreaderwriter('sensor data.csv')
