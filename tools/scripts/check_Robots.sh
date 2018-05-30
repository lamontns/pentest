#!/bin/bash

# Global Variables
robots=$domain.txt
break="==============================================================="
# End of Global Variables
clear
echo
echo
echo -n "Enter the domain: " # -n just removes the trailing new line
read domain # read accepts the user unput and stores it in variable domain
echo -n "Where would you like to store the files?: "
read location
echo
echo "You have targeted" $domain "and will store the files in" $location
read -p "Press <ENTER> to continue."

if [ -z $domain, $location ];then
	echo
	echo "You did not enter a domain"
	exit
fi

wget $domain/robots.txt -O $location/robots.txt &
sleep 10
cat $location/robots.txt | grep Disallow | awk '{print $2}' > $location/$robots 2>/dev/null
sleep 1
firefox &
sleep 4

for i in $(cat $location/$robots); do
	firefox -new-tab $domain$i &
	sleep 1
done
echo $break
echo "Starting cleanup"
echo $break
rm $location/rob* 2>/dev/null
rm $location/$robots 2>/dev/null
echo $break
echo "Cleanup complete"
echo $break