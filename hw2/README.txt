Author: HIMCHAN YUN(111322206), Stony Brook University CSE363

HW2 dnspoison.py

This program is a python program that sniff packets and poison DNS so that a victim cannot reach
certain URLs, rather it reaches to the attacker's page.

To run the program use the following example command on command prompt,

    $ sudo python dnspoison.py [-i interface] [-f hostnames] expression

This program is built on 32-bit Kali Linux v2020.1 with python 2 or 3
python-scapy must be installed to run the program.

** Before you run, type the following two commands:

    #iptables -I OUTPUT -j NFQUEUE --queue-num 0
    #iptables -I INPUT -j NFQUEUE --queue-num 0