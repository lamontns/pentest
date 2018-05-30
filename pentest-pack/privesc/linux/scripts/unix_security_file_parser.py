#!/usr/bin/env python
from upc.parser.sshd_config import sshd_config
from upc.parser.sysctl import sysctl
from upc.parser.sudoers import sudoers
from upc.parser.passwd import passwd
from upc.parser.selinux import selinux
from upc.parser.group import group
from upc.parser.snmpd import snmpd
from upc.parser.syslog import syslog
from upc.parser.mount import mount
from upc.parser.ifconfig import ifconfig
from upc.parser.shadow import shadow
from upc.parser.env import env
from upc.parser.netstat import netstat
from upc.parser.permissions import permissions
from upc.parser.unix_privesc_check import unix_privesc_check
from upc.knowledge_base import knowledge_base 
from wpc.report.report import report
from upc.parseOptions import parseOptions
import upc.utils
import re

# [ wpc notes ]
# We take the reporting engine from windows-privesc-check with minor mods:
# replace wpc/conf.py with our own issues
# remove wpc/*Acl*

# [ Dependencies ]
# apt-get install python-lxml

# unpack tar ball

# need to parse files in a particular order to ensure
# knowlegebase (kb) is populated with info required by
# each parser
#tarball = 1

#for file in upc.parser.order_files(tarball):
#    info, issues = upc.parser.auto_parse(file)

# Parse command line arguments
options = parseOptions()

report = report()
issues = report.get_issues()
kb = knowledge_base()

if options.group_file:
    s = group()
    s.parse(options.group_file, issues, kb)
    
if options.passwd_file:
    s = passwd()
    s.parse(options.passwd_file, issues, kb)
    
if options.shadow_file:
    s = shadow()
    s.parse(options.shadow_file, issues, kb)
    
if options.env_file:
    s = env()
    s.parse(options.env_file, issues, kb)
    
if options.netstat_file:
    s = netstat()
    s.parse(options.netstat_file, issues, kb)
    
if options.ifconfig_file:
    s = ifconfig()
    s.parse(options.ifconfig_file, issues, kb)
    
if options.sudoers_file:
    s = sudoers()
    s.parse(options.sudoers_file, issues, kb)
    
if options.perms_file:
    s = permissions()
    s.parse(options.perms_file, issues, kb)
    
if options.sshd_config_file:
    s = sshd_config()
    s.parse(options.sshd_config_file, issues, kb)
    
if options.sysctl_file:
    s = sysctl()
    s.parse(options.sysctl_file, issues, kb)
    
if options.upc_file:
    s = unix_privesc_check()
    s.parse(options.upc_file, issues, kb)

if options.mount_file:
    s = mount()
    s.parse(options.mount_file, issues, kb)

if options.snmpd_file:
    s = snmpd()
    s.parse(options.snmpd_file, issues, kb)

files = {}    
if options.directory:
    for f in upc.utils.dirwalk(options.directory):
        m = re.search("/group$", f)
        if m:
            print "[+] Parsing %s as group file" % f
            files["group"] = f
    
        print "[D] Processing %s" % f
        
        m = re.search("/passwd$", f)
        if m:
            m2 = re.search("security/passwd$", f)
            if not m2:
                print "[+] Parsing %s as passwd file" % f
                files["passwd"] = f
    
        m = re.search("[^g]shadow$", f)
        if m:
            print "[+] Parsing %s as shadow file" % f
            files["shadow"] = f
    
        m = re.search("[^g]env$", f)
        if m:
            print "[+] Parsing %s as env file" % f
            files["env"] = f
    
        m = re.search("^netstat", f)
        if m:
            print "[+] Parsing %s as netstat file" % f
            files["netstat"] = f
    
        m = re.search("/upc(?:-[^/]+)$", f)
        if m:
            print "[+] Parsing %s as upc file" % f
            files["upc"] = f
            files["ifconfig"] = f # contains ifconfig output if we can't find it elsewhere
    
        m = re.search("ifconfig", f)
        if m:
            print "[+] Parsing %s as ifconfig file" % f
            files["ifconfig"] = f
    
        m = re.search("sshd_config$", f)
        if m:
            print "[+] Parsing %s as sshd_config file" % f
            files["sshd_config"] = f
    
        m = re.search("/sysctl-a", f)
        if m:
            print "[+] Parsing %s as sysctl file" % f
            files["sysctl"] = f
    
        m = re.search("sudoers$", f)
        if m:
            print "[+] Parsing %s as sudoers file" % f
            files["sudoers"] = f
    
        m = re.search("(perms.txt|all-files.txt)$", f)
        if m:
            print "[+] Parsing %s as permissions file" % f
            files["perms"] = f

        m = re.search("/syslog", f)
        if m:
            print "[+] Parsing %s as syslog file" % f
            files["syslog"] = f

        m = re.search("/selinux", f)
        if m:
            print "[+] Parsing %s as selinux file" % f
            files["selinux"] = f

        m = re.search("/mount", f)
        if m:
            print "[+] Parsing %s as mount file" % f
            files["mount"] = f

        m = re.search("/snmpd.conf", f)
        if m:
            print "[+] Parsing %s as snmpd file" % f
            files["snmpd"] = f

# We need to parse the files in the particular order
file_order = []
file_order.append("group")
file_order.append("passwd")
file_order.append("shadow")
file_order.append("env")
file_order.append("netstat")
file_order.append("ifconfig")
file_order.append("upc")
file_order.append("sshd_config")
file_order.append("sysctl")
file_order.append("sudoers")
file_order.append("perms")
file_order.append("syslog")
file_order.append("selinux")
file_order.append("mount")
file_order.append("snmpd")

for name in file_order:
    if not name in files.keys():
        continue
    
    f = files[name]
    
    if name == "group":
        s = group()
        s.parse(f, issues, kb)
    
    if name == "passwd":
        s = passwd()
        s.parse(f, issues, kb)
    
    if name == "shadow":
        s = shadow()
        s.parse(f, issues, kb)
    
    if name == "env":
        s = env()
        s.parse(f, issues, kb)
    
    if name == "netstat":
        s = netstat()
        s.parse(f, issues, kb)
    
    if name == "ifconfig":
        s = ifconfig()
        s.parse(f, issues, kb)
    
    if name == "upc":
        s = unix_privesc_check()
        s.parse(f, issues, kb)
    
    if name == "sshd_config":
            s = sshd_config()
            s.parse(f, issues, kb)
    
    if name == "sysctl":
            s = sysctl()
            s.parse(f, issues, kb)
    
    if name == "sudoers":
            s = sudoers()
            s.parse(f, issues, kb)
    
    if name == "perms":
            s = permissions()
            s.parse(f, issues, kb)
    
    if name == "syslog":
            s = syslog()
            s.parse(f, issues, kb)
    
    if name == "selinux":
            s = selinux()
            s.parse(f, issues, kb)
    
    if name == "mount":
            s = mount()
            s.parse(f, issues, kb)
    
    if name == "snmpd":
            s = snmpd()
            s.parse(f, issues, kb)
    
filename = "%s.html" % options.report_file_stem
print "[+] Saving report file %s" % filename
f = open(filename, 'w')
f.write(report.as_html())
f.close()

filename = "%s.txt" % options.report_file_stem
print "[+] Saving report file %s" % filename
f = open(filename, 'w')
f.write(report.as_text())
f.close()
