#!/bin/sh

DIR=`hostname`
echo "[+] Starting data collection for ${DIR}"
echo "[+] Creating directory: ${DIR}"
mkdir ${DIR}
chmod 700 ${DIR}
cd ${DIR}
echo "[+] Saving output from: netstat -na"
netstat -na 2>/dev/null > netstat-na
echo "[+] Saving output from: cat /etc/passwd"
cat /etc/passwd 2>/dev/null > passwd
echo "[+] Saving output from: cat /etc/group"
cat /etc/group 2>/dev/null > group
echo "[+] Saving output from: cat /etc/shadow"
cat /etc/shadow 2>/dev/null > shadow
echo "[+] Saving output from: cat /etc/security/passwd"
cat /etc/security/passwd 2>/dev/null > security-passwd
echo "[+] Saving output from: cat /etc/sudoers"
cat /etc/sudoers 2>/dev/null > sudoers
echo "[+] Saving output from: cat /etc/ssh/sshd_config"
cat /etc/ssh/sshd_config 2>/dev/null > sshd_config
echo "[+] Saving output from: sysctl -a"
sysctl -a 2>/dev/null > sysctl-a
echo "[+] Saving output from: mount"
mount 2>/dev/null > mount
echo "[+] Saving output from: cat /etc/snmp/snmpd.conf"
cat /etc/snmp/snmpd.conf 2>/dev/null > snmpd.conf
echo "[+] Saving output from: ifconfig -a"
ifconfig -a 2>/dev/null > ifconfig-a
echo "[+] Saving output from: set"
set 2>/dev/null > set
echo "[+] Saving output from: find / -ls (very slow!)"
find / -ls 2>/dev/null > all-files.txt
echo "[+] Data collection complete"
echo "[+] Creating tar ball: tar cf ${DIR}.tar ${DIR}"
cd ..
tar cf ${DIR}.tar ${DIR}
echo "[+] Finished"
echo "[+] IMPORTANT:"
echo "[+]    * copy ${DIR}.tar to a safe location - contains sensitive data"
echo "[+]    * remove ${DIR} directory and ${DIR}.tar"
