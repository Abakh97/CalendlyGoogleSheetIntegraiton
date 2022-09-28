import pygsheets
import pandas as pd
from datetime import datetime
import pytz
import Datefinder

index_labels = ['Aidana', 'Alexis', 'Andre Atkins', 'Andrea Serna', 'Andrew', 'Bonnie', 'Cadence', 'Caleb', 'Carlous', 'Chris Smit', 'Christopher Pepino', 'Daria', 'David', 'Destiny', 'Erica', 'Gray', 'Gus', 'Harper', 'Heather', 'Isaiah', 'Jake', 'Jim', 'Jamie', 'Jennifer', 'Jordan Moore', 'Jordan Mrad', 'Karen', 'Keenan', 'Lauren', 'Marilyn', 'Maya', 'Miriah', 'Sasha', 'Paul', 'Rhonda', 'Luci','Ryan', 'Sherece', 'Steve', 'Tamara', 'Tanya', 'Tara', 'Tomas', 'Tracy', 'Abid']
#date_list = ['9/1/2022', '9/2/2022', '9/3/2022','9/4/2022', '9/5/2022', '9/6/2022', '9/7/2022', '9/8/2022', '9/9/2022', '9/10/2022', '9/11/2022', '9/12/2022', '9/13/222', '9/14/2022', '9/15/2022', '9/16/2022', '9/17/2022', '9/18/2022', '9/19/2022', '9/20/2022', '9/21/2022', '9/22/2022', '9/23/2022', '9/24/2022', '9/25/2022', '9/26/2022', '9/27/2022', '9/28/2022', '9/29/2022', '9/30/2022', '9/31/2022']
gc = pygsheets.authorize(service_file='creds.json')
#df = pd.DataFrame(index=index_labels, columns=date_list)

def main(datetime_str, name):
    sh = gc.open('Care Seeker ALL Master Tracker')
    loc = []
    wks = sh[0]
    index = 10 
    new_char = ' '
    datetime_str = datetime_str[:index] + new_char + datetime_str[index+1:]
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f%z')
    my_datetime_PST = datetime_obj.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    x = my_datetime_PST.split()
    date = x[0]
    day = date.split('-')
    matchday = day[2]
    print(matchday)
    fname = name
    let = Datefinder.main(matchday)
    loc.append(let)
    for i in index_labels:
        if i in fname:
            num = index_labels.index(i)+2
            loc.append(num)
            print(loc)
            cell = "".join(str(l) for l in loc)
            print(cell)
            print("name found")
            print(fname)
            wks.update_value(cell, 'X')
                
    #df['name'] = ['John', 'Steve', 'Sarah', 'Abid']
    
    
    sh = gc.open('PY to Gsheet Test')
    
#J-AM

#main('2022-09-22T02:00:00.000000Z', 'Sherece Bakhtiyar')