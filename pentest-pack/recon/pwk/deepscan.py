#!/usr/bin/env python
import xml.etree.ElementTree
from libnmap.parser import NmapParser
import subprocess
from subprocess import *
import sys
import os
import re
import reconf
from reconf import *

if len(sys.argv) != 2:
    print "Usage: deeprecon.py <ip address>"
    sys.exit(0)

ip_address = sys.argv[1].strip()

def chkfolders():
    dpths = [reconf.rootpth,reconf.labpath,reconf.rsltpth,reconf.exampth,reconf.nmappth]
    for dpth in dpths:
        if not os.path.exists(dpth):
                os.makedirs(dpth)

def multProc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip,port))
    jobs.append(p)
    p.start()
    return

def dnsEnum(ip_address, port):
    print "INFO: Detected DNS on %s %s" % (ip_address, port)
    if port.strip() == "53":
       SCRIPT = "./dnsrecon.py -ip %s" % (ip_address)     
       subprocess.call(SCRIPT, shell=True)
    return

def searchsploitEnum(ip_address):
    print "INFO: Searching for known exploits for %s" % (ip_address)
    SCRIPT = "./vulnrecon.py %s" % (ip_address)
    subprocess.call(SCRIPT, shell=True)
    return

def httpEnum(ip_address, port):
    print "INFO: Gathering additional HTTP information %s:%s" % (ip_address, port)
    HTTPSCAN = "nmap -Pn -n -vv -sC -p %s --script=%s -oA %s/%s_http %s" % (port, reconf.httpnse, reconf.exampth, ip_address, ip_address)
    results = subprocess.check_output(HTTPSCAN, shell=True)
    HTTPHDRS = "nmap -Pn -n -vv -p %s --script=%s -oA %s/%s_%s_httpheader %s" % (port, 'http-headers', reconf.exampth, ip_address, port, ip_address)
    results = subprocess.check_output(HTTPHDRS, shell=True)

def httpsEnum(ip_address, port):
    print "INFO: Gathering additional HTTPS information %s:%s" % (ip_address, port)
    HTTPSCANS = "nmap -Pn -n -vv -sC -p %s --script=%s -oA %s/%s_https %s" % (port, reconf.httpnse, reconf.exampth, ip_address, ip_address)
    results = subprocess.check_output(HTTPSCANS, shell=True)
    HTTPHDRS = "nmap -Pn -n -vv -p %s --script=%s -oA %s/%s_%s_httpheader %s" % (port, 'http-headers', reconf.exampth, ip_address, port, ip_address)
    results = subprocess.check_output(HTTPHDRS, shell=True)

def hgreEnum(ip_address, port):
    print "INFO: Searching for sensitive information on %s:%s" % (ip_address, port)
    HTTPGREP = "nmap -Pn -n -vv -oA %s/%s_httpgrep -p %s %s --script http-grep --script-args http-grep.builtins" % (reconf.exampth, ip_address, port, ip_address)
    results = subprocess.check_output(HTTPGREP, shell=True)

def niktoEnum(ip_address, port)
    print "INFO: Performing Nikto scan on %s:%s" % (ip_address, port)
    NIKTOSCAN = "nikto -host %s -p %s > %s._nikto" % (ip_address, port, ip_address)
    results = subprocess.check_output(NIKTOSCAN, shell=True)

def dirbEnum(ip_address):
    print "INFO: Brute force dictionary attack for directories on %s" % (ip_address)
    DIRBUST = "./dirbust.py -ip %s -ss" % (ip_address) 
    subprocess.call(DIRBUST, shell=True)

def oracleEnum(ip_address, port):
    print "INFO: Detected Oracle on %s:%s" % (ip_address, port)
    ORACLESCAN = "nmap -vv -Pn -p %s --script=oracle-enum-users,oracle-sid-brute -oA %s/%s_oracle.xml %s" % (port, reconf.exampth, ip_address, ip_address)
    results = subprocess.check_output(ORACLESCAN, shell=True)

def mssqlEnum(ip_address, port):
    print "INFO: Detected MS-SQL on %s:%s" % (ip_address, port)
    print "INFO: Performing nmap mssql script scan for %s:%s" % (ip_address, port)
    MSSQLSCAN = "nmap -vv -Pn -p %s --script=ms-sql-info,ms-sql-config,ms-sql-dump-hashes --script-args=mssql.instance-port=1433,smsql.username-sa,mssql.password-sa -oA %s/%s_mssql.xml %s" % (port, reconf.exampth, ip_address, ip_address)
    subprocess.call(MSSQLSCAN, shell=True)

def mysqlEnum(ip_address, port):
    print "INFO: Detected MySQL on %s:%s" % (ip_address, port)
    print "INFO: Performing nmap mssql script scan for %s:%s" % (ip_address, port)
    MYSQLSCAN = "nmap -vv -Pn -p %s --script=mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 -oA %s/%s_mysql.xml %s" % (port, reconf.exampth, ip_address, ip_address)
    subprocess.call(MYSQLSCAN, shell=True)
    HYDRA = "hydra -L %s -P %s -f -t 1 -o %s/%s_mysqlhydra.txt %s mysql" % (reconf.usrlst, reconf.pwdlst, reconf.exampth, ip_address, ip_address)
    results = subprocess.check_output(HYDRA, shell=True)
    resultarr = results.split("\n")
    for result in resultarr:
    	if "login:" in result:
        	print "[*] Valid ftp credentials found: " + result
    MEDUSA = "medusa -L %s -P %s -f -t 1 -o %s/%s_mysqlhydra.txt %s mysql" % (reconf.usrlst, reconf.pwdlst, reconf.exampth, ip_address, ip_address)
    results = subprocess.check_output(HYDRA, shell=True)
    resultarr = results.split("\n")
    for result in resultarr:
    	if "login:" in result:
        	print "[*] Valid credentials found: " + result
    

def sshEnum(ip_address, port):
    print "INFO: Detected SSH on %s:%s" % (ip_address, port)
    SCRIPT = "./sshrecon.py %s %s" % (ip_address, port)
    subprocess.call(SCRIPT, shell=True)
    return

def snmpEnum(ip_address, port):
    print "INFO: Detected snmp on %s:%s" % (ip_address, port)
    SCRIPT = "./snmprecon.py %s" % (ip_address)
    subprocess.call(SCRIPT, shell=True)
    return

def smtpEnum(ip_address, port):
    print "INFO: Detected smtp on %s:%s" % (ip_address, port)
    if port.strip() == "25":
       SCRIPT = "./smtprecon.py %s" % (ip_address)
       subprocess.call(SCRIPT, shell=True)
    else:
       print "WARNING: SMTP detected on non-standard port, smtprecon skipped (must run manually)"
    return

def smbEnum(ip_address, port):
    print "INFO: Detected SMB on %s:%s" % (ip_address, port)
    SCRIPT = "./smbrecon.py %s" % (ip_address)
    subprocess.call(SCRIPT, shell=True)
    return

def tbdEnum(tbd):
    print "\033[1;31m[!]\033[1;m To be developed: %s" % (tbd) 
    return

def ftpEnum(ip_address, port):
    print "INFO: Detected ftp on %s:%s" % (ip_address, port)
    SCRIPT = "./ftprecon.py %s %s" % (ip_address, port)
    subprocess.call(SCRIPT, shell=True)
    return

def altOSEnum(ip_address):
    print "INFO: Alternative OS detection for %s" % (ip_address)
    OSTRY = "nmap -O --osscan-guess %s" % (ip_address)
    results = subprocess.check_output(OSTRY, shell=True)
    rsltarray = results.split('\n')
    for line in rsltarray:
        if re.search('Running',line):
                return line.split(':')[1].strip()

def opnPORTS(ip_address):
   try:
        fnmap = "%s/%s.nmap" % (reconf.exampth, ip_address)
        print "\033[1;31m [!] \033[0;m Parsing %s for identifying open ports" % (fnmap)
        if os.path.isfile(fnmap):
                CATS = "cat %s | grep open | cut -d'/' -f1 | sort -h | tr '\n' ','" % (fnmap)
                results = subprocess.check_output(CATS, shell=True)
                results = results.rstrip(',')
        else:
                print "\033[1;38m [!] \033[0;m %s is missing.  Run nmap with the -oA option" % (fnmap)
        return results
   except:
        pass

def vulnCHK(ip_address):
   oprts = opnPORTS(ip_address)
   print "\033[1;31m [!] \033[0;m Ports found: %s " % (oprts)
   if oprts == "":
   	VCHK = "nmap -sV -vv -A -sC -Pn -n --script vuln --script-args=unsafe=1 -oA '%s/%s_vuln' %s" % (reconf.exampth, ip_address, ip_address)
   else:
   	VCHK = "nmap -sV -vv -A -sC -Pn -n -p %s --script vuln --script-args=unsafe=1 -oA '%s/%s_vuln' %s" % (oprts, reconf.exampth, ip_address, ip_address)
   print "[+] Executing - %s" % (VCHK)
   print "\033[1;33m[*]\033[0;m Running general vuln scans for " + ip_address
   subprocess.call(VCHK, shell=True)

def exploitCHK(ip_address):
   oprts = opnPORTS(ip_address)
   print "\033[1;31m [!] \033[0;m Ports found: %s " % (oprts)
   if oprts == "":
   	ECHK = "nmap -sV -vv -Pn -n --script exploit --script-args=unsafe=1 -oA '%s/%s_exploit' %s" % (reconf.exampth, ip_address, ip_address)
   else:
   	ECHK = "nmap -sV -vv -Pn -n -p %s --script exploit --script-args=unsafe=1 -oA '%s/%s_exploit' %s" % (oprts, reconf.exampth, ip_address, ip_address)
   print "[+] Executing - %s" % (ECHK)
   print "\033[1;33m[*]\033[0;m Attempting to exploit " + ip_address
   subprocess.call(ECHK, shell=True)

if __name__=='__main__':
    
    vulnCHK(ip_address)
    exploitCHK(ip_address)

    print "[*] Parsing %s/%s.xml" % (reconf.exampth, ip_address)
    xmlfile = "%s/%s.xml" % (reconf.exampth, ip_address)
    tree = xml.etree.ElementTree.parse(xmlfile)

    rep = NmapParser.parse_fromfile(xmlfile)
    for _host in rep.hosts:
    	host = ', '.join(_host.hostnames)
    	ip = (_host.address)

    serv = []
    for attb in tree.iter('service'): 
 	#print attb.attrib
    	name = attb.attrib.get('name')
	serv.append(name)

    try: 
    	for osmatch in _host.os.osmatches:
    		osys = osmatch.name
    except IOError:
        osys = 'Microsoft'
    else:
        osys = altOSEnum(ip_address)

    print "OS: %s" % (osys)

    if re.match('Microsoft', osys) and osys != "":
	cnt=0
    	for services in _host.services:
		print
        	print "\033[1;33m[+]\033[1;m Port: "'{0: <5}'.format(services.port), "Service: "'{0: <10}'.format(serv[cnt])
		print 
		# 21
		if re.search('ftp', serv[cnt]):
			print "[+] Running ftpEnum %s, %s" % (ip_address, services.port)
			ftpEnum(ip_address, services.port)
		# 22
		if re.search('ssh',serv[cnt]):
			print "[+] Running sshEnum %s, %s" % (ip_address, services.port)
			sshEnum(ip_address, services.port)
		# 25
		if re.search('smtp',serv[cnt]):
			print "[+] Running smtpEnum %s, %s" % (ip_address, services.port)
			smtpEnum(ip_address, services.port)
		# 53
		if re.search('domain',serv[cnt]):
			print "[+] Running dnsEnum %s, %s" % (ip_address, services.port)
			dnsEnum(ip_address, services.port)
		# 80
		if not re.search('https',serv[cnt]) and re.search('http',serv[cnt]):
			print "[+] Running httpEnum %s, %s" % (ip_address, services.port)
			httpEnum(ip_address, services.port)
			hgreEnum(ip_address, services.port)
		# 135
		if re.search('msrpc', serv[cnt]):
			print "[+] Running rpcEnum %s, %s" % (ip_address, services.port)
			tbdEnum(serv[cnt])
		# 139
		if re.search('netbios-ssn', serv[cnt]):
			print "[+] Running rpcEnum %s, %s" % (ip_address, services.port)
			tbdEnum(serv[cnt])
		# 161-162
		if re.search('snmp',serv[cnt]):
			print "[+] Running snmpEnum %s, %s" % (ip_address, services.port)
			snmpEnum(ip_address, services.port)
		# 443
		if re.search('https',serv[cnt]) or re.search('ssl\/http',serv[cnt]):
			print "[+] Running httpsEnum %s, %s" % (ip_address, services.port)
			httpsEnum(ip_address, services.port)
			hgreEnum(ip_address, services.port)
		# 445
		if re.search('microsoft-ds', serv[cnt]):
			print "[+] Running smbEnum %s, %s" % (ip_address, services.port)
			smbEnum(ip_address, services.port)
		# 1433-1434
		if re.search('ms-sql', serv[cnt]):
			print "[+] Running mssqlEnum %s, %s" % (ip_address, services.port)
			mssqlEnum(ip_address, services.port)
		# 1521
		if re.search('oracle', serv[cnt]):
			print "[+] Running oracleEnum %s, %s" % (ip_address, services.port)
			oracleEnum(ip_address, services.port)
		# 3306
		if re.search('mysql', serv[cnt]):
			print "[+] Running mysqlEnum %s, %s" % (ip_address, services.port)
			mysqlEnum(ip_address, services.port)
		cnt += 1
	print
   	print "INFO: Deep scan completed for " + ip_address
    else:
	print "OS Unknown: %s" % (osys)
 

    if re.match('Linux', osys) and osys != "":
	cnt = 0
	for services in _host.services:
		print "Port: "'{0: <5}'.format(services.port), "State: "'{0: <5}'.format(services.state), "Protocol: "'{0: <2}'.format(services.protocol), "Service: "'{0:<10}'.format(serv[cnt])
	cnt += 1
    else:
	print "OS: Unknown %s" % (osys)

