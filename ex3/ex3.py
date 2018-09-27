#!/usr/bin/env python3

from sys import argv, exit
import hashlib

def main():
	toHash = 'rizzosaporito'
	bitsToMatch = 8
	lastT = ''
	lastH = ''

	print(toHash)
	print(encrypt_string(toHash))
	
	tortoise = encrypt_string(toHash)[:bitsToMatch]
	hare = tortoise
	print(tortoise)
	print(hare)

	while 1:
		lastT = tortoise
		tortoise = encrypt_string(tortoise)[:bitsToMatch]
		lastH = hare
		hare = encrypt_string(encrypt_string(hare)[:bitsToMatch])[:bitsToMatch]
		if hare == tortoise:
			break

	print("Found match with %d bits: %s	%s\n" %(bitsToMatch * 4,tortoise,hare))
	print("Last tortoise: %s	Last hare: %s\n" %(lastT,lastH))

def encrypt_string(stringToHash):
	shaHash = hashlib.sha256(stringToHash.encode()).hexdigest()
	return shaHash

if __name__ == "__main__":
	exit(main())
