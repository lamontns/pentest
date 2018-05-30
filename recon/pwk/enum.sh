#!/bin/sh
#
iface=$1
ipadd=$2
range=$3
wks=$4

# In the lab the iface should be tap0
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

if [ $# -eq 0 ]; then
  echo "${RED} [!] Frogot something? ${NC} Need arguments, e.g.:"
  echo "${NC} enum.sh eth0 10.3.1.162 10.3.1.162 /root/projects/"
  exit
fi

wkip="IP$(echo ${ipadd} | tr -d '.')"
wksp="${wks}/${wkip}"

#arp-scan -l

if [ -d $wksp ]; then
  echo "${GREEN} [*] ${NC} Workspace ${wksp} is ready."
else
  echo "${YELOW} [!] ${NC} Workspace ${wksp} is being setup."
  mkdir ${wksp}
fi

echo "${RED} [!!!] ${NC} Starting enumeration against ${ipadd}"

if [ ! -f ${wksp}/nmap_qt ]; then
  # Quick Scans
  echo "${GREEN} [*] ${NC} TCP Quick Scans."
  nmap -Pn -n -sS --stats-every 3m --max-retries 1 --max-scan-delay 20 --defeat-rst-ratelimit -T4 -p1-65535 -oX ${wksp}/nmap_qt ${ipadd}
  echo "${GREEN} [*] ${NC} UDP Quick Scans."
  nmap -Pn -n --top-ports 1000 -sU --stats-every 3m --max-retries 1 -T3 -oX ${wksp}/nmap_qu ${ipadd}
fi

# Get the open TCP Ports from Quick Scans (nmap_qt)
ports=$(cat ${wksp}/nmap_qt | grep portid | grep protocol=\"tcp\" | cut -d'"' -f4 | paste -sd ",")
echo "${YELLOW} [!] ${NC} The following TCP Ports are open: ${WHITE} ${ports}"

if [ -z "${ports}" ]; then
  echo "${YELLOW} [!] ${NC} No ports open, exiting."
  exit
fi

# Guess versions full
if [ ! -f ${wksp}/nmap_ft.xml ]; then
  echo "${GREEN} [*] ${NC} Identifying protocol versions of each port."
  #nmap -Pn -n -sSV -T1 -p${ports} --version-intensity 9 -A -oA ${wksp}/nmap_ft ${ipadd}
fi

# Guess versions light
if [ ! -f ${wksp}/nmap_lt ]; then
  echo "${GREEN} [*] ${NC} Identifying protocol versions of each TCP port (Light)."
  nmap -n --open -p${ports} --version-light -oN ${wksp}/nmap_lt ${ipadd}
fi

if [ ! -f /usr/share/nmap/scripts/banner-plus.nse ]; then
  echo "${YELLOW} [!] ${NC} Grabbing HD Moore's banner-plus.nse."
  cd /root
  git clone https://github.com/hdm/scan-tools.git
  cp /root/scan-tools/nse/banner-plus.nse /usr/share/nmap/scripts/
fi

# Guess version ALL
echo "${GREEN} [*] ${NC} Identifying protocol versions of each TCP port (ALL)."
nmap -e ${iface} -n --open -p${ports} --version-all -oN ${wksp}/nmap_version_all ${ipadd}
echo "${GREEN} [*] ${NC} Identifying protocol versions of each TCP port (-sV)."
nmap -e ${iface} -v -n --open -p${ports} -sV -oN ${wksp}/nmap_sV ${ipadd}

# Grab Banners
echo "${GREEN} [*] ${NC} Grabbing Banners..."
nmap -Pn -n -p ${ports} --script=banner-plus -oA ${wksp}/nmap_banner ${ipadd}

# Run specialized scans
for port in $(echo $ports | sed "s/,/ /g"); do 
  echo "${GREEN} [*] ${NC} Checking for anything interesting on ${port}."
  if [ $port -eq 22 ]; then
    nmap -n -Pn -p ssh -sV -A -oN ${wksp}/nmap_ssh ${ipadd}
    hydra -v -l root -P /root/wordlist/SecLists/Passwords/Common-Credentials/best110.txt -t 3 -o ${wksp}/hydra_ssh ssh://${ipadd} 
  fi
  if [ $port -eq 80 ] || [ $port -eq 443 ]; then
    #nmap -n -Pn --script http-enum -oN ${wksp}/nmap_${port} ${ipadd}

    curl -i http://${ipadd}:${port}/robots.txt >> ${wksp}/curl_robots_${port}

    nikto -output ${wksp}/niktoi_${port} -host ${ipadd}
    if [ $port -eq 80 ]; then
      dirb http://${ipadd} -o ${wksp}/dirb_${port}
    else
      dirb https://${ipadd} -o ${wksp}/dirb_${port}
    fi
  fi
  if [ $port -eq 111 ]; then
    nmap -n -Pn -p 111 -sV -A -oN ${wksp}/nmap_${port} ${ipadd}
  fi
  if [ $port -eq 135 ]; then
    nmap -n -Pn -p 135 -A -oN ${wksp}/nmap_${port} ${ipadd}
  fi
  if [ $port -eq 139 ] || [ $port -eq 445 ]; then
    #nmap -n -Pn -p $port -A -oN ${wksp}/nmap_${port} ${ipadd}
    enum4linux ${ipadd} >> ${wksp}/e4l_${port}
    smbclient -N --list=${ipadd} >> ${wksp}/smb_${port}
  fi
  if [ $port -eq 3306 ]; then
    nmap -n -Pn -p 3306 --script=mysql-enum -oN ${wksp}/nmap_${port} ${ipadd}
  fi
    
if [ ${port} -eq 8008 ]; then
  echo "${GREEN} [*] ${NC} Get device information XML."
  curl http://${ipadd}:8008/ssdp/device-desc.xml >> ${wksp}/curl_xml

  echo "${GREEN} [*] ${NC} Get detailed device information json"
  curl http://${ipadd}:8008/setup/eureka_info?options=detail >> ${wksp}/curl_json

  echo "${GREEN} [*] ${NC} Scan for available wifi"
  curl http://${ipadd}:8008/setup/scan_results >> ${wksp}/curl_wifi

  echo "${GREEN} [*] ${NC} Get supported time zone"
  curl http://${ipadd}:8008/setup/supported_timezones >> ${wksp}/curl_timezone

  echo "${GREEN} [*] ${NC} Get information about current app"
  curl -H “Content-Type: application/json” http://${ipadd}:8008/apps/YouTube -X GET >> ${wksp}/curl_currentapp

#send youtube video to chromecast:
#curl -H “Content-Type: application/json” http://${ipadd}:8008/apps/YouTube -X POST -d ‘v=oHg5SJYRHA0’

#kill current running app:
#curl -H “Content-Type: application/json” http://${ipadd}:8008/apps/YouTube -X DELETE

#reboot the chromecast dongle:
#curl -H “Content-Type: application/json” http://${ipadd}:8008/setup/reboot -d ‘{“params”:”now”}’ -X POST

#factory default reset the chromecast dongle:
#curl -H “Content-Type: application/json” http://${ipadd}:8008/setup/reboot -d ‘{“params”:”fdr”}’ -X POST
fi
done
