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
	output=[None]*16	
	iv=[None]*16
	output=[None]*16
	bytearray(output)
	with open(encryptedfile, 'rb') as f:
		for i in range(16):
			iv[i]=bytearray(f.read(1))
		print(iv)
		while f != '':
			msg=f.read(16)
			msg=bytearray(decipher.decrypt(msg))
			for x in range(16):
				output[x]=iv[x] ^ msg[x] 
			with open(outputfile,'w') as o:
				for x in range(16):
					o.write(str(output[x]))
			iv=msg









if __name__ == "__main__":
	exit(main())
