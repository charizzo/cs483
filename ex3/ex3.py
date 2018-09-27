#!/usr/bin/env python3

from sys import argv, exit
import hashlib

def main():
	toHash = 'rizzosaporito'
	hexCharsToMatch = 8
	lastT = ''
	lastH = ''

	print(toHash)
	
	tortoise = encrypt_string(toHash)#[:hexCharsToMatch]
	hare = tortoise
	print(hare)

	while 1:
		lastT = tortoise
		tortoise = encrypt_string(tortoise[:hexCharsToMatch])#[:hexCharsToMatch]
		lastH = hare
		hare = encrypt_string(encrypt_string(hare[:hexCharsToMatch])[:hexCharsToMatch])#)[:hexCharsToMatch])[:hexCharsToMatch]
		if hare[:hexCharsToMatch] == tortoise[:hexCharsToMatch]:
			break

	print("Found match with %d bits:\n" %(hexCharsToMatch * 4))
	print("T: %s\nH: %s\n" %(tortoise, hare))
	print("Last tortoise: %s\nLast hare: %s\n" %(lastT,lastH))

def encrypt_string(stringToHash):
	shaHash = hashlib.sha256(stringToHash.encode()).hexdigest()
	return shaHash

if __name__ == "__main__":
	exit(main())
