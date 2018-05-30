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

wkip="IP$(echo ${ipadd} | tr -d '.')"
wksp="${wks}/${wkip}"

arp-scan -l

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

# Guess versions full
if [ ! -f ${wksp}/nmap_ft.xml ]; then
  echo "${GREEN} [*] ${NC} Identifying protocol versions of each port."
  #nmap -Pn -n -sSV -T1 -p${ports} --version-intensity 9 -A -oA ${wksp}/nmap_ft ${ipadd}
fi

# Guess versions light
if [ ! -f ${wksp}/nmap_lt ]; then
  echo "${GREEN} [*] ${NC} Identifying protocol versions of each TCP port (Light)."
  #nmap ${iface} -n -Pn -sV -sC --open -p${ports} --version-light -A -sS -oN ${wksp}/nmap_lt ${ipadd}
  echo "${GREEN} [*] ${NC} Identifying protocol versions of each UDP port (Light)."
  #nmap ${iface} -n -Pn -sV -sC --version-light -A -sU -oN ${wksp}/nmap_lu ${ipadd}
fi

# Run specialized scans
for port in $(echo $ports | sed "s/,/ /g"); do 
  echo "${GREEN} [*] ${NC} Checking for anything interesting on ${port}."
    curl -i http://${ipadd}:${port}/robots.txt >> ${wksp}/curl_robots_${port}
    nikto -output ${wksp}/niktoi_${port} -host ${ipadd}
    dirb http://${ipadd} -o ${wksp}/dirb_${port}
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
