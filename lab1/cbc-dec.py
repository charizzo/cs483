#!/usr/bin/env python3
from Crypto.Cipher import AES
from sys import argv, exit
import sys
from io import BytesIO
import binascii

def main():

	keyfile=sys.argv[1]
	encryptedfile=sys.argv[2]
	outputfile=sys.argv[3]

	f=open(keyfile,"r")
	hex_key=f.read()
	key=bytes.fromhex(hex_key)
	decipher = AES.new(key, AES.MODE_ECB)

	o=open(outputfile,'w')
	output=[1]*16

	with open(encryptedfile, 'rb') as f:
		iv=bytearray(f.read(16).strip())
	#	print(len(iv))
		while 1:
			msg=f.read(16).strip()
			if msg == bytes('','utf-8'):
				break
			msg=bytearray(decipher.decrypt(msg))
			print(msg)
			for x in range(16):
				output[x]=iv[x] ^ msg[x] 
				o.write(chr(output[x]))
			iv=msg









if __name__ == "__main__":
	exit(main())
