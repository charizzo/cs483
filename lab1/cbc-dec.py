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

	o=open(outputfile,'wb')
	output=[1]*16
	final=[]

	with open(encryptedfile, 'rb') as f:
		iv=bytearray(f.read(16))
		while 1:
			msg=f.read(16)
			if msg == bytes('','utf-8'):
				break
			msg2=bytearray(decipher.decrypt(msg))
			for x in range(16):
				output[x]=iv[x] ^ msg2[x] 
				final.append(output[x])
			iv=msg

	shred = final[len(final) - 1]
	if shred == 0:
		o.write(str.encode(final))
	else:
		final = final[:-shred]
		o.write(bytes(final))




if __name__ == "__main__":
	exit(main())
