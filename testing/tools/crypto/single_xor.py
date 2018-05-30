#!/usr/bin/env python
# 
# breaks single xor key

def score(text):
	charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
	p = 0
	for s in text:
		if s in charset or s == ' ' or s == '\'':
			p+=1
	return p

def xor(s1, s2):
	res = ""
	for i in range(0, len(s1)):
		res += chr(ord(s1[i]) ^ ord(s2[i%len(s2)]))

	return res

def main():
	# Example - I hope you love Taylor too
	plain = """Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby I'm just gonna shake, shake, shake, shake, shake
I Shake it off, I shake it off"""
	key = "x"

	cipher = xor(plain, key)

	# Having cipher, we gonna crack it

	best = ""
	b = 0
	
	for i in range(0, 256):
		c = xor(cipher, chr(i))
		if score(c) > b:
			b = score(c)
			best = c

	print best

if __name__ == "__main__":
	main()
