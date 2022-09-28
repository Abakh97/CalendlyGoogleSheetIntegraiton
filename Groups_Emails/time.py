from datetime import datetime 
import pytz
datetime_str = '2022-09-23T02:00:00.000000Z'
index = 10
new_char = ' '
datetime_str = datetime_str[:index] + new_char + datetime_str[index+1:]

datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f%z')

my_datetime_PST = datetime_object.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
print(type(datetime_object))
print(datetime_object)
print(type(my_datetime_PST))
print(my_datetime_PST)
x = my_datetime_PST.split()
date = x[0]
day = date.split('-')
matchday = day[2]
print(matchday) 
#print(datetime_str)


