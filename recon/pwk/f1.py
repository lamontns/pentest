#!/usr/bin/env python
import subprocess
import multiprocessing
from multiprocessing import *
import os
import sys
import re
import reconf
from reconf import *
import time
from functools import wraps
import argparse
import ipaddr
import nmapxml
from nmapxml import *
import ftputil

parser = argparse.ArgumentParser(description='Run a short or verbose dirb scan')
parser.add_argument('-ip', action='store', required=True, help='IP Address to be assessed')

args = parser.parse_args()
try:
        ip_address = ipaddr.IPAddress(args.ip)
except:
        print "Try again..."
        sys.exit()

ip_address = str(ip_address)

def anonLogin(ip_address):
	try:
		ftp = ftputil.FTPHost(ip_address, "anonymous", "a@a.com")
        	print "[+] %s - Anonymous FTP is Permitted" % ip_address
        	return True
    	except Exception, e:
        	print "[-] %s - Anonymous FTP not allowed" % ip_address
        	return False

def bruteLogin(ip_address):
	BLOGIN = "./brutepwd.py -ip %s -s ftp -hy" % ip_address
	results = subprocess.check_output(BLOGIN, shell=True)
	print results

    	return ("anonymous", "a@a.com")

outfile = "%s/%s_ftpwalk.txt" % (reconf.rsltpth, ip_address)
f = open(outfile, 'w')
if anonLogin(ip_address):
	ftp = ftputil.FTPHost(ip_address, "anonymous", "a@a.com")
else:
	if os.path.isfile("%s/%s_ftp_hydra.txt" % (reconf.rsltpth, ip_address)):
		
	else:
		usern, password = bruteLogin(ip_address)
		ftp = ftputil.FTPHost(ip_address, "anonymous", "a@a.com")
try:
    recursive = ftp.walk("/",topdown=True,onerror=None)
    for root,dirs,files in recursive:
	for dlst in dirs:
		results = "%s\n" % dlst
		if dlst != "":
	 		f.write(results)	
	for fname in files:
		results = "%s/%s\n" % (root, fname)
		if fname != "":
			f.write(results)
		if re.search(r'^(index)[.](htm|html|asp|php)', fname):
			print "[+] Found default page %s at %s" % (fname, root)
except:
	pass

ftp.close
