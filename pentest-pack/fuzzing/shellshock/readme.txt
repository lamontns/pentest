--------------------------------------------------------------------------
.____________     _____ __________  _________.__                   __
|   \_   ___ \   /     \\______   \/   _____/|  |__   ____   ____ |  | __
|   /    \  \/  /  \ /  \|     ___/\_____  \ |  |  \ /  _ \_/ ___\|  |/ /
|   \     \____/    Y    \    |    /        \|   Y  (  <_> )  \___|    <
|___|\______  /\____|__  /____|   /_______  /|___|  /\____/ \___  >__|_ \
            \/         \/                 \/      \/            \/     \/

ICMPShock | A scanning tool for the ShellShock bash vulnerability.
Written by Peter Kim <Author, The Hacker Playbook>
                     <CEO, Secure Planet LLC>
--------------------------------------------------------------------------



< About >

    ICMPShock is a tool designed to determine whether or not a target web server contains cgi scripts
    that could provide an attack vector for exploitation of the "ShellShock" bash vulnerability.

    This is determined by injecting crafted environment variables into various fields 
    of a POST request to 1 or more target web servers defined in a file. The value of these environment
    variables is a "ping" command to the listening IP address the user specifies.

    By using a tool such as tcpdump to listen for ICMP requests, the user can determine whether or not 
    a target server is vulnerable by observing whether or not an ICMP request was sent from the target
    to the listening machine the user specifies. If the user recieves an ICMP packet from the target, they can assume 
    that the current version of the bash interpreter installed on the target is vulnerable.


< Usage >

    Before execution of this script, a tool such as tcpdump will need to be started to see results from the target.
    An example of this would be-
    
    sudo tcpdump -nni eth0 -e icmp[icmptype] == 8
    
    After this is executed, the user will be ready to use ICMPShock.

    The format to use this tool is-

    python icmpshock.py <listening IP> <targets_file>

    The user will be prompted to start the scanner, and the value of the listening IP and number of threads
    will be reflected in STDOUT before the script is executed.

    The targets file holds the target addresses, one line per target address-

    ============
    target1
    target2
    target3
    ...snip...
    ============

    The file "Updated_list_Cgi_files.txt" is the file which holds paths to CGI scripts to append to the address
    of the web server. These values are from RAFT and detectify.com, but a different file can be used if specified in the 
    code of the script (just uncomment the line #cgi_file = sys.argv[3], and uncomment the "for" loop at the bottom
    of the script that uses "cgi_file" instead of "Updated_list_Cgi_files.txt"). If using sys.argv[3], then the command would look like-

    python icmpshock.py <listening IP> <targets_file> <cgi_path_file>

    An example-
   
    python icmpshock.py 127.0.0.1 target_list.txt cgi_test_paths.txt
