import requests

url = "https://api.calendly.com/scheduled_events/754b1844-9668-40ba-8d7e-646daa2f053d"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjYxMjkyOTUyLCJqdGkiOiIyN2ExNThmYi01YTVmLTRkZjYtYjA5NC1hNjQxZjk0MWUzM2UiLCJ1c2VyX3V1aWQiOiJhMTBiZDBlNS1kZWFkLTQ1ZGYtYjY1YS1jZjhjNDIzMWRiMTQifQ.0eQSO0LBRsLjFPk23yD5XHNyuRhUeBQUm9Mou9zw7mSrurgF-2JuSMKe_iUctWDUCN0VmELv9AYOQS7jo3jLKA"
    }

params = {'organization': 'https://api.calendly.com/organizations/42e02138-60e6-4e41-96f7-2fddde91d3ae'}

response = requests.request("GET", url, headers=headers, params=params)
date = response.json()
#print(date)
eventDate = date["resource"]["start_time"]

#print(eventDate)
print(response.text)
