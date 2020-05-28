Author: HIMCHAN YUN(111322206), Stony Brook University CSE363

HW1 sniffer.py

This program is a python program that sniffs TLS and HTTP traffic using Scapy library.
When TLS Client hello packet and HTTP Requests packets will only be prited.

To run the program use the following example command on command prompt,

    $ sudo python sniffer.py [-i interface] [-r tracefile] expression

This program is built on 32-bit Kali Linux v2020.1 with python 2 or 3
python-scapy must be installed to run the program.

Example:
    The following output is printed with the command:

        $ sudo python sniffer.py -r example.pcap

    (example.pcap is captured from accessing file:///usr/share/kali-defaults/web/homepage.html and https://www.google.com using wireshark
    IP address is replaced with xxx because of security issue)

20-02-22 11:51:9 HTTP 10.0.2.xxx:47292 -> 172.232.19.xxx:80 detectportal.firefox.com GET /success.txt
20-02-22 11:51:8 TLS v1.3 10.0.2.xxx:36808 -> 13.33.87.xxx:443 ▒snippets.cdn.mozilla.net
20-02-22 11:51:8 TLS v1.3 10.0.2.xxx:57760 -> 172.217.10.xxx:443 www.google.com
20-02-22 11:51:9 HTTP 10.0.2.xxx:41516 -> 172.217.11.xxx:80 ocsp.pki.goog POST /gts1o1
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:40336 -> 172.217.xxx.99:443 www.gstatic.com
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:40338 -> 172.217.xxx.99:443 www.gstatic.com
20-02-22 11:51:9 HTTP 10.0.2.xxx:41516 -> 172.217.11.xxx:80 ocsp.pki.goog POST /gts1o1
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:52084 -> 172.217.xxx.238:443 ▒clients5.google.com
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:52082 -> 172.217.xxx.238:443 ▒clients5.google.com
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:52080 -> 172.217.xxx.238:443 ▒clients5.google.com
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:36692 -> 172.217.xxx.14:443 apis.google.com
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:46032 -> 172.217.xxx.34:443 adservice.google.com
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:38060 -> 172.217.xxx.170:443  afebrowsing.googleapis.com
20-02-22 11:51:9 HTTP 10.0.2.xxx:41516 -> 172.217.11.xxx:80 ocsp.pki.goog POST /gts1o1
20-02-22 11:51:9 HTTP 10.0.2.xxx:41538 -> 172.217.11.xxx:80 ocsp.pki.goog POST /gts1o1
20-02-22 11:51:9 TLS v1.3 10.0.2.xxx:46036 -> 172.217.10.xxx:443  oogleads.g.doubleclick.net
20-02-22 11:51:9 HTTP 10.0.2.xxx:41516 -> 172.217.11.xxx:80 ocsp.pki.goog POST /gts1o1
