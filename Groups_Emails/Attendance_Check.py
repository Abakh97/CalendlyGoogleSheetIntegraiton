import json 
import os
import requests
import gsheets
import pygsheets
from datetime import datetime
from datetime import date
from datetime import timedelta
import pytz

yesterday = date.today() - timedelta(days = 1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
print(yesterday_str)
print(type(yesterday_str))
max_time = "23:59:00"
min_time = "0:01:00"
format = '%Y-%m-%d %H:%M:%S'
max_str = yesterday_str + " " + max_time
min_str = yesterday_str + " " + min_time
local_max = datetime.strptime(max_str, format)
local_min = datetime.strptime(min_str, f)
print(max_str)
print(min_str)


#datetime = 
'''
url = "http://api.calendly.com/scheduled_events"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjYxMjkyOTUyLCJqdGkiOiIyN2ExNThmYi01YTVmLTRkZjYtYjA5NC1hNjQxZjk0MWUzM2UiLCJ1c2VyX3V1aWQiOiJhMTBiZDBlNS1kZWFkLTQ1ZGYtYjY1YS1jZjhjNDIzMWRiMTQifQ.0eQSO0LBRsLjFPk23yD5XHNyuRhUeBQUm9Mou9zw7mSrurgF-2JuSMKe_iUctWDUCN0VmELv9AYOQS7jo3jLKA"
    }

params = {'organization': 'https://api.calendly.com/organizations/42e02138-60e6-4e41-96f7-2fddde91d3ae',
          'max_start_time': '',
          'min_start_time': ''
          }
'''