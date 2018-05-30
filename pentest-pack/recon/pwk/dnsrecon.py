#!/usr/bin/env python
import subprocess
from subprocess import *
import sys
import os
import re
import reconf
from reconf import *
import argparse
import ipaddr
import nmapxml
from nmapxml import *
import dns.name
import dns.query
import dns.dnssec
import dns.message
import dns.resolver
import dns.rdatatype
import dns.zone

parser = argparse.ArgumentParser(description='Run a DNS scan')
parser.add_argument('-ip', action='store', required=True, help='IP Address to be assessed')

args = parser.parse_args()
try:
        ip_address = ipaddr.IPAddress(args.ip)
	ip_address = str(ip_address)
except:
        print "Not a valid IP. Try again..."
        sys.exit()

def turnc_ad(s, d, n=3):
	return d.join(s.split(d)[:n])

def turnc_bc(s, d, n=1):
	return d.join(s.split(d)[n:])

sbn = turnc_ad(ip_address, '.') 

print "SBN %s" % sbn

dnsfile = "%s/%s_DNSDIS.xml" % (reconf.exampth, sbn) 
if not os.path.isfile(dnsfile):
	DNSDIS = "nmap -sV -vv -Pn -n -p U:53,T:53 --open -oA %s/%s_DNSDIS %s" % (reconf.exampth, sbn, reconf.fulliprng)
	subprocess.call(DNSDIS, shell=True)

wbxml = "%s/%s_DNSDIS.xml" % (reconf.exampth, sbn)
info = minidom.parse(wbxml)
dnslst = nmapxml.get_All_IP(info).split(',')

myresolver = dns.resolver.Resolver()
myresolver.nameservers = dnslst 
reverseip = '.'.join(ip_address.split('.')[::-1])
ptrlookup = reverseip + '.in-addr.arpa'
hostname = str(myresolver.query(ptrlookup,"PTR")[0]).rstrip('.')
domain = turnc_bc(hostname, '.') 
domindot = domain + '.'

request = dns.message.make_query(domindot, dns.rdatatype.DNSKEY, want_dnssec=True)

outfile = "%s/%s_dnschk" % (reconf.rsltpth, ip_address)
with open(outfile, 'a') as file:
	file.write("Hostname: %s" % hostname)
	file.write("Domain: %s" % domain)

	for nserver in dnslst:
		response = dns.query.udp(request, nserver)
		file.write("Response %s" % response)
		file.write("Answer: %s" % response.answer)
		file.write("Response Code: %s" % response.rcode())
		DNSCHK = "nmap -vv -sn -Pn %s -oA %s/%s_DNSZONE --script dns-check-zone --script-args='dns-check-zone.domain=%s'" % (nserver, reconf.rsltpth, ip_address, domain)
		subprocess.call(DNSCHK, shell=True)
		axfr = dns.query.xfr(nserver, domindot, lifetime=5)
		try:
			zone = dns.zone.from_xfr(axfr)
			if zone == "":
				file.write("Success: %s @ %s" % (domain, nserver))
				for name, node in zone.nodes.items():
					rdatasets = node.rdatasets
					for rdataset in rdatasets:		
						file.write("%s %s" % name, rdataset)
			else:
				continue
		except:
			continue
