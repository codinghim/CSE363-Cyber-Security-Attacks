import sys
import time
from datetime import datetime
from scapy.all import *
from scapy.layers.http import HTTPRequest
load_layer("tls")
load_layer("http")

args = sys.argv

# This function returns String that describes TLS version number given version byte is given as int
def checkTLSVersion(versionInt):
    if versionInt == 772:
        return "v1.3"
    elif versionInt == 771:
        return "v1.2"
    elif versionInt == 770:
        return "v1.1"
    elif versionInt == 769:
        return "v1.0"
    else:
        return "version not found"

flag = 0
interface = ""
tracefile = ""
expression = ""
count = 0
for argct in range(len(args)-1):
    argcount = argct + 1
    if flag != 1:
        if args[argcount].lower() == '-i':
            #interface argument
            flag = 1
            interface = args[argcount+1]
        
        elif args[argcount].lower() == '-r':
            #tracefile argument
            flag = 1
            tracefile = args[argcount+1]

        else:
            expression = args[argcount]
    else:
        flag = 0

if interface == "":
    interface = "eth0"

pkts = []
i = 0
# if tracefile == "":
#     if expression == "":
#             pkts = sniff(count = 500, iface = interface)
#         else:
#             pkts = sniff(count = 500, iface = interface, filter = expression)
# else:
#     #trace file
#     pkts = rdpcap(tracefile)

while i<1000:
    if tracefile == "":
        if expression == "":
            pkts = sniff(count = 500, iface = interface)
        else:
            pkts = sniff(count = 500, iface = interface, filter = expression)
    else:
        #trace file
        pkts = rdpcap(tracefile)
        i = 1000
    for p in pkts:
        # if a packet has TLS layer
        if p.haslayer("TLS"):
            # if the packet type is a handshake
            if p[TLS].type == 22:
                # if the packet is a Client Hello message
                if p[TLS].msg[0].msgtype == 1:
                    gmttime = time.gmtime(p[TLS].time)
                    srcIP = str(p[IP].src)
                    dstIP = str(p[IP].dst)
                    sport = str(p[TCP].sport)
                    dport = str(p[TCP].dport)
                    tlsver = ""
                    for a in p[TLS].msg[0].ext:
                        if a.type == 43:
                            tlsver = checkTLSVersion(a.versions[0])
                    if tlsver == "":
                        tlsver = checkTLSVersion(p[TLS].msg[0].version)
                    servername = str(p[TLS].msg[0].ext[0])
                    print time.strftime('%y-%m-%d %I:%M:%-S', gmttime) + ' TLS ' + tlsver + " " + srcIP + ":" + sport + " -> " + dstIP + ":" + dport + " " + servername
        elif p.haslayer(HTTPRequest):
            gmttime = time.gmtime()
            srcIP = str(p[IP].src)
            dstIP = str(p[IP].dst)
            sport = str(p[TCP].sport)
            dport = str(p[TCP].dport)
            method = str(p[HTTPRequest].Method)
            dsthost = str(p[HTTPRequest].Host)
            requestURI = str(p[HTTPRequest].Path)
            print time.strftime('%y-%m-%d %I:%M:%-S', gmttime) + ' HTTP ' + srcIP + ":" + sport + " -> " + dstIP + ":" + dport + " " + dsthost + " " + method + " " + requestURI
    i = i + 1

#HTTP 1) method used, 2) dest hostname, 3) requested URI
#TLS 1) Client Hello message 2) TLS version number 3) dest host name(Server Name Indication field)
