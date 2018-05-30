# Single Byte XOR

## 1) Scheme
Encryption works by xoring plaintext with single byte XOR.

Encrypting: THIS IS DATA WE WANT TO ENCRYPT
```
plaintext  53454352455420444154412057452057414e5420544f20454e4352595054
xor        4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b4b
----------------------------------------------------------------
ciphertext 180e08190e1f6b0f0a1f0a6b1c0e6b1c0a051f6b1f046b0e050819121b1f

```
Ciphertext (in hex): 180e08190e1f6b0f0a1f0a6b1c0e6b1c0a051f6b1f046b0e050819121b1f

## 2) Breaking encryption
It can be bruteforced by trying all possible values and calculacting score of the text.

## 3) Simple script for breaking single byte XOR:

```python
#!/usr/bin/env python

import sys

def score(text):
	charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
	p = 0
	for s in text:
		if s in charset or s == ' ' or s == '\'':
			p+=1
	return p

# function that performs XOR operation on two strings
def xor(s1, s2):
	res = ""
	for i in range(0, len(s1)):
		res += chr(ord(s1[i]) ^ ord(s2[i%len(s2)]))

	return res

def main():
	best = ""
	b = 0

    # bruteforcing all possible values
	for i in range(1, 256):
		c = xor(sys.argv[1].decode('hex'), chr(i))
		if score(c) > b:
			b = score(c)
			best = c

    print "Plaintext: {}".format(best)

if __name__ == "__main__":
	main()
```

## 4) Usage:

```
./break.py 180e08190e1f6b0f0a1f0a6b1c0e6b1c0a051f6b1f046b0e050819121b1f
Plaintext: SECRET DATA WE WANT TO ENCRYPT
```

