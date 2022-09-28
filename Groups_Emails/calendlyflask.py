import json 
import os
import google
import requests
import gsheets

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/newEvent', methods=['POST'])
def webhook():
    if request.method == 'POST':
        appointments = request.json
        eventUrl = appointments["payload"]["event"]
        print(appointments)
        print(eventUrl)
        
        headers= {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjYxMjkyOTUyLCJqdGkiOiIyN2ExNThmYi01YTVmLTRkZjYtYjA5NC1hNjQxZjk0MWUzM2UiLCJ1c2VyX3V1aWQiOiJhMTBiZDBlNS1kZWFkLTQ1ZGYtYjY1YS1jZjhjNDIzMWRiMTQifQ.0eQSO0LBRsLjFPk23yD5XHNyuRhUeBQUm9Mou9zw7mSrurgF-2JuSMKe_iUctWDUCN0VmELv9AYOQS7jo3jLKA"}
        params = {"organization": "https://api.calendly.com/organizations/42e02138-60e6-4e41-96f7-2fddde91d3ae"}
        url = eventUrl
        date = requests.request("GET", url, headers=headers, params=params)
        eventinfo = date.json ()
        client = appointments["payload"]["name"]
        eventDate = eventinfo["resource"]["start_time"]
        gsheets.main(eventDate, client)
        #print(date.text)
        return "Webhook Recieved"
if __name__ == '__main__':
    app.run()