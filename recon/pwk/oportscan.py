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

if len(sys.argv) != 2:
    print "Usage: deeprecon.py <ip address>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
folders = [reconf.wordlst, reconf.vulns]

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

@fn_timer
def dirbEnum(prot, ip_address, port):
	found = []
	url = "%s://%s:%s" % (prot, ip_address, port)
	print "INFO: Starting dirb scan for " + url
	agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)"
	for folder in folders:
	    for filename in os.listdir(folder):
		outfile = "-o %s/%s_%s_dirb_%s" % (reconf.exampth, ip_address, port, filename)
		DIRBSCAN = "dirb %s %s/%s %s -S -r" % (url, folder, filename, outfile)
		try:
		    results = subprocess.check_output(DIRBSCAN, shell=True)
		    resultarr = results.split("\n")
		except:
		    pass

def vpnstatus():
   return int(os.popen('ifconfig tap0 | wc -l').read().split()[0])

if __name__=='__main__':
    # Check if VPN to the Offsec lab is up
    if not vpnstatus() > 1:
        print "You forgot to connect to the lab"
        sys.exit()

    print "[*] Parsing %s/%s.nmap" % (reconf.exampth, ip_address)

    fnmap = "%s/%s.nmap" % (reconf.exampth, ip_address)
    print "\033[1;31m [!] \033[0;m Parsing %s for identifying open ports" % (fnmap)
    with open(fnmap, 'r') as searchfile:
	for line in searchfile:
		if 'open' in line and re.search('http|ssl/http|https', line):
			#print line
			port = re.split('\s+', line)[0]
			port = re.split('\/', port)[0].strip()
			prot = re.split('\s+', line)[2].strip()
			prot = re.split('\?', prot)[0].strip()
			if 'ssl/http' in line: prot = 'https'
			
			dirbEnum(prot, ip_address, port)
