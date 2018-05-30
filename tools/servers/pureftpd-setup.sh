#!/bin/bash

if [ ! type curl &> /dev/null ]; then
  echo -e "[\e[31m+\e[39m] You need to install pure-ftpd befor running this script!"
  echo -e "[\e[31m+\e[39m] apt-get install pure-ftpd"
  echo -e "[\e[31m+\e[39m] or something like that."
  exit
fi

if [ -z $1 ]; then
  echo "[*] Simple pure-ftfpd setup script"
  echo "[*] Usage: $0 <username>"
  echo ""
  exit 0
fi

groupadd ftpgroup
useradd -g ftpgroup -d /dev/null -s /etc ftpuser
pure-pw useradd $1 -u ftpuser -d /ftphome
pure-pw mkdb
cd /etc/pure-ftpd/auth/
ln -s ../conf/PureDB 60pdb
mkdir -p /ftphome
chown -R ftpuser:ftpgroup /ftphome/
service pure-ftpd restart
