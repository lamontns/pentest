#!/usr/bin/env python
#
# lucyoa@sage~/$ ./rot.py "YRIRY GJB CNFFJBEQ EBGGRA" 13
# LEVEL TWO PASSWORD ROTTEN
# 
# for i in $(seq 1 20); do ./rot.py "YRIRY GJB CNFFJBEQ EBGGRA" $i; done
# :)

import sys
import string

def rot(cipher, rotation):
	""" HERE U CAN CHANGE ALPHABET! ADD LETTERS NUMBERS ETC """
	charset = string.ascii_uppercase

	res = ""
	for c in cipher:
		if c != " ":
			res += charset[(((ord(c)-65)+rotation)%len(charset))]
		else:
			res += " "
	return res

def usage():
	print "%s <cipher> <rotation>" % sys.argv[0]
	exit(0)

def main():
	if len(sys.argv) != 3:
		usage()

	cipher = sys.argv[1]
	rotation = sys.argv[2]
	print rotation + " - " + rot(cipher, int(rotation))

if __name__ == "__main__":
	main()
