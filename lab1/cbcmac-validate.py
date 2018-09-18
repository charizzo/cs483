#!/usr/bin/env python3
from Crypto.Cipher import AES
from sys import argv, exit
import sys


def main():
	
	keyfile=sys.argv[1]
	messagefile=sys.argv[2]
	tagfile=sys.argv[3]

	with open(keyfile,'rb') as k:
		keyfile=k.read()
	with open(messagefile,'rb') as m:
		message=m.read()

	lengthmessage=len(message)
	print(message)

	for i in range(0,lengthmessage,16):
		for j in range(i):
			print(j)




if __name__ == "__main__":
	exit(main())

