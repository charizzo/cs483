#!/usr/bin/env python2.7

from sys import argv, exit
import hashlib

def main():
	toHash = 'rizzosaporito'
	hexCharsToMatch = 12
	lastT = ''
	lastH = ''
	counter = 0
	x = ''
	x_prime = ''

	print(toHash)
	
	tortoise = encrypt_string(toHash)
	hare = encrypt_string(tortoise[:hexCharsToMatch])

	while tortoise[:hexCharsToMatch] != hare[:hexCharsToMatch]:
		tortoise = encrypt_string(tortoise[:hexCharsToMatch])
		hare = encrypt_string(encrypt_string(hare[:hexCharsToMatch])[:hexCharsToMatch])
		counter += 1

	print("Found match with %d bits:\n" %(hexCharsToMatch * 4))
	print("T: %s\nH: %s\n" %(tortoise, hare))

	x_prime = tortoise
	x = toHash

	newX = encrypt_string(x)
	newX_Prime = encrypt_string(x_prime[:hexCharsToMatch])

	while newX[:hexCharsToMatch] != newX_Prime[:hexCharsToMatch]:
		x = newX
		x_prime = newX_Prime
		newX = encrypt_string(x[:hexCharsToMatch])
		newX_Prime = encrypt_string(x_prime[:hexCharsToMatch])
	
	print("Found match!")
	print("%s and %s\nhash to %s\n" %(x[:hexCharsToMatch], x_prime[:hexCharsToMatch], newX[:hexCharsToMatch]))

def encrypt_string(stringToHash):
	shaHash = hashlib.sha256(stringToHash.encode()).hexdigest()
	return shaHash

if __name__ == "__main__":
	exit(main())
