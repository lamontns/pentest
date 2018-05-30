#!/usr/bin/env python
import subprocess
import multiprocessing
from multiprocessing import * 
import os
import sys
import time 
import nmap
import re
import reconf
from reconf import *
import time
from functools import wraps

def hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return("%d:%02d:%02d:" % (h, m, s))
 
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s" %
               (function.func_name, hms(t1-t0))
              )
        return result
    return function_timer

def multProc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip,port))
    jobs.append(p)
    p.start()
    return

def TCPScan(ip_address):
   ip_address = ip_address.strip()
   TCPSCAN = "nmap -sV -vv -Pn -O -sS -T4 -p- -oA '%s/%s' %s"  % (reconf.exampth, ip_address, ip_address)
   print "\033[1;33m[*]\033[0;m Running general TCP nmap scans for " + ip_address
   subprocess.check_output(TCPSCAN, shell=True)

def UDPScan(ip_address):
   ip_address = ip_address.strip()
   UDPSCAN = "nmap -sV -vv -Pn -O -sU -T4 --top-ports 20 -oA '%s/%sU' %s" % (reconf.exampth, ip_address, ip_address)
   print "\033[1;33m[*]\033[0;m Running general UDP nmap scans for " + ip_address
   subprocess.check_output(UDPSCAN, shell=True)

def dualScan(ip_address):
   TCPScan(ip_address)
   #UDPScan(ip_address)

@fn_timer
def deepScan(ip_address):
   DSCAN = "./deepscan.py %s" % (ip_address)
   print "\033[1;33m[*]\033[0;m Digging deeper into " + ip_address
   subprocess.call(DSCAN, shell=True)

def chkfolders():
    dpths = [reconf.rootpth,reconf.labpath,reconf.rsltpth,reconf.exampth,reconf.nmappth]
    for dpth in dpths:
        if not os.path.exists(dpth):
                os.makedirs(dpth)

def createList(ipadr):
   nm = nmap.PortScanner()
   args = "-sP -PS -n -oG %s " % (reconf.opth)
   nm.scan(ipadr,arguments=args)
   fo = open(reconf.olst,"w")
   with open(reconf.opth) as input:
        for line in input:
                line = line.split(" ")
                if re.match('[a-zA-Z]',line[1]) is None:
                        fo.write("%s\n" % (line[1]))
   fo.close()

def vpnstatus():
   return int(os.popen('ifconfig tap0 | wc -l').read().split()[0])

if __name__=='__main__': 
   # Check if VPN to the Offsec lab is up
   if not vpnstatus() > 1:
        print "You forgot to connect to the lab"
	sys.exit()

   # Make sure the folders exists
   chkfolders()
   
   # Create list of active IPs
   createList(reconf.iprange)

   print "Intel Gathering"
   jobs = []
   f = open(reconf.olst, 'r') 
   for scanip in f:
       p = multiprocessing.Process(target=dualScan, args=(scanip,))
       jobs.append(p)
   f.close()

   for j in jobs:
	j.start()

   for j in jobs:
       j.join()
       print "%s.exitcode = %s" % (j.name, j.exitcode)

'''
   print "Deeper Dive"
   jobs = []
   f = open(reconf.olst, 'r') 
   for scanip in f:
       p = multiprocessing.Process(target=deepScan, args=(scanip,))
       jobs.append(p)
   f.close()

   for j in jobs:
	j.start()

   for j in jobs:
       j.join()
       print "%s.exitcode = %s" % (j.name, j.exitcode)
'''
