#!/usr/bin/env python
import subprocess
import sys
import os
import reconf
from reconf import *

if len(sys.argv) != 3:
    print "Usage: ftprecon.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Performing nmap FTP script scan for " + ip_address + ":" + port
FTPSCAN = "nmap -sV -Pn -vv -p %s --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -oA %s/%s_ftp.nmap %s" % (port, reconf.exampth, ip_address, ip_address)
subprocess.check_output(FTPSCAN, shell=True)

print "INFO: Performing password disovery on FTP against " + ip_address 
BRUTE = "./brutepwd.py -ip %s -a" % ip_address
subprocess.call(BRUTE, shell=True)
