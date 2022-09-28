import requests 

url = "https://api.calendly.com/webhook_subscriptions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjYxMjkyOTUyLCJqdGkiOiIyN2ExNThmYi01YTVmLTRkZjYtYjA5NC1hNjQxZjk0MWUzM2UiLCJ1c2VyX3V1aWQiOiJhMTBiZDBlNS1kZWFkLTQ1ZGYtYjY1YS1jZjhjNDIzMWRiMTQifQ.0eQSO0LBRsLjFPk23yD5XHNyuRhUeBQUm9Mou9zw7mSrurgF-2JuSMKe_iUctWDUCN0VmELv9AYOQS7jo3jLKA"
}


params = {'organization' :'https://api.calendly.com/organizations/42e02138-60e6-4e41-96f7-2fddde91d3ae'}

data = {
        "url":"https://98c4-99-82-224-220.ngrok.io/newEvent",
        "events":["invitee.created", "invitee.canceled"],
        "organization":"https://api.calendly.com/organizations/42e02138-60e6-4e41-96f7-2fddde91d3ae",
        "scope":"organization"
        }

response = requests.request("POST", url, headers=headers, json = data)

print(response.text)