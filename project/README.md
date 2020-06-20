HIMCHAN YUN(11322206)
##Project Covert Command and control

Commands and control which is also called as CNC or C2 is the type of attack
that establishes connection between a server and a client. When the server
sends a list of commands, commands run covertly on client side to retrieve data.

### Two Versions of program
### 1) servercnc1.py and clientcnc1.py

    sudo python servercnc1.py -c [commands]
    sudo python clientcnc1.py

Basics of this program is that client keeps sending a ping request to server.
Whenever server which uses socket to listen on traffics receives a packet,
it validates a packet whether it is from a client and if it is, it sends back
either a ping pong reply or a list of commands to run on client. Client who receives
a list of commands runs on it.

Features:   1) I used client key to detect if the packet is indeed from a client or a server
            2) Fernet encryption is used to hide raw string so that it is hard to be detected

### 2) servercnc2.py and clientcnc2.py

    sudo python3 servercnc2.py -c [commands]
    python clientcnc2.py

Features: This is using email as a intermediate to send and receive a large
amount of code which is obvious to be caught if it in the payload.

Server sends a email to a gmail account with a body of list of commands and sends
the email address to client via packet. Client receives the email address and using Gmail
API, it reads the contents of the first email in the inbox and runs that commands on client.


### Things to know

There are some parts to be hard-coded such as client key, fernet key, email address.
Credentials from email is required for using Gmail API which has instruction on the bottom
of this file.

### Pcap trace files
commands1-1.pcapng -> running servercnc1 and clientcnc1 with commands1
commands1-2.pcapng -> running servercnc1 and clientcnc1 with commands2
commands2-1.pcapng -> running servercnc2 and clientcnc2 with commands1


### install scapy
sudo apt-get update
sudo apt-get install python-pip
pip install scapy
pip install cryptography

### Gmail api instruction
https://developers.google.com/gmail/api/quickstart/python

