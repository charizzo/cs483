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
	final=""

	with open(encryptedfile, 'rb') as f:
		iv=f.read(16).strip()
		intiv=int.from_bytes(iv, byteorder='big')
		while 1:
			msg=bytearray(f.read(16).strip())
			if msg == bytes('','utf-8'):
				break
			iv2=bytearray(decipher.decrypt(iv))
#			print(iv2)
			print(len(iv2))
			print(len(msg))
			for x in range(13):
				output[x]=iv2[x] ^ msg[x] 
				final+=(chr(output[x]))
		#		print(chr(output[x]))
			intiv+=1

	shred=ord(final[len(final)-1])
	if shred == 0:
		o.write(final)
	else:
		final = final[:-shred]
		print(shred)
		o.write(final)
	




if __name__ == "__main__":
	exit(main())
