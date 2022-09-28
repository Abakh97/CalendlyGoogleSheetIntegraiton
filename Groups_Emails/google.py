import httplib2
import os
import oauth2client 
from oauth2client import client, tools, file
import base64
from email.mime.muiltipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient import errors 
from googleapiclient import discovery 
import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase

SCOPES = 'http://www.googleapis.com/auth.gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'CALLRAIL Notification System'

def main():
    {
     print("appointments recieved")
     }
def get_credentials():
    home_dir = os.path.expanduer('~')
    credentials_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credentials_dir):
        os.makedirs(credentials_dir)
    credentials_path = os.path.join(credentials_dir, 'callrail-notifier..json')
    store = oauth2client.file.Storage(credentials_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print("Storing credentials to " + credentials_path)
    return credentials

def sendMessage(sender, to, subject, msgHtml, msgPlain, attachmentFile=None):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmails', 'v1', http=http)
    if attachmentFile:
        message1 = CreateMessageHtml(sender, to, subject, msgHtml, msgPlain)
    else:
        message1 = CreateMessageHtml(sender, to, subject, msgHtml, msgPlain)
    #result = SendMessageInternal(service, user_id, message1)
    #return result





def CreateMessageHtml(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg["Subject"] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body

def create():
    print ("create")
    
        