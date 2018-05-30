#!/usr/bin/env python

import winrm

s = winrm.Session('192.168.31.216', auth=('IEuser', 'toor'))
r = s.run_cmd('ipconfig', ['/all'])

print r.status_code
print r.std_out
print r.std_err
