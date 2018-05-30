#!/usr/bin/env python
import subprocess
import sys
import reconf
from reconf import *

if len(sys.argv) != 2:
    print "Usage: rpcrecon.py <ip address>"
    sys.exit(0)

ip_address = sys.argv[1]

RPC = "rpcclient -U %s %s" % ("", ip_address)
results = subprocess.check_output(RPC, shell=True).strip()

if results != "":
	print results
