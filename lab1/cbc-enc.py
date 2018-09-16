#!/usr/bin/env python3

from sys import argv,exit
from Crypto.Cipher import AES
from Crypto import Random
import os.path

def main():
	if len(argv) != 7:
		print("Usage: ./cbc-enc.py -k <key file> -i <input file> -o <output file>")
		raise Exception("Bad Command Line Args")

	fin = open(argv[2],"r")
	hexKey = fin.read().strip()
	fin.close()

	fout = open(argv[6],"wb+")

	IV = bytearray(os.urandom(16))
	blockCipher = AES.new(bytes.fromhex(hexKey),AES.MODE_ECB)
	flag = True
	first = True

	fout.write(IV)
	print("IV:")
	print(IV)
	print();
	with open(argv[4],"rb") as inputFile:
		while 1:
			messageBlock = bytearray(inputFile.read(16).strip())
			if(len(messageBlock) != 16 and messageBlock != bytes('','utf-8')):
				flag = False;
				padding = 16 - len(messageBlock)
				for i in range(0,padding):
					messageBlock += padding.to_bytes(1,byteorder='big')

			if(messageBlock == bytes('','utf-8')):
				break

			if(first):	
				print(messageBlock)
				for i in range(0, 16):
					IV[i] ^= messageBlock[i]

				print(IV)
				cipherText = blockCipher.encrypt(bytes(IV))
				fout.write(cipherText)
				first = False
				lastMessageBlock = bytearray(cipherText)
				print(lastMessageBlock)
				print()
			else:
				print(messageBlock)
				for i in range(0,16):
					messageBlock[i] ^= lastMessageBlock[i]
				
				print(messageBlock)
				temp = blockCipher.encrypt(bytes(messageBlock))
				fout.write(temp)
				lastMessageBlock = bytearray(temp)
				print(lastMessageBlock)
				print()

	if(flag):
	#	for i in range(0,16):
	#		messageBlock[i] = (16).to_bytes(1,byteorder='big')
		messageBlock = bytearray([0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10])
		
		print(messageBlock)
#		print(type(messageBlock))
#		print(type(lastMessageBlock))

		for i in range(0,16):
			messageBlock[i] ^= lastMessageBlock[i]

		print(messageBlock)
		cipherText = blockCipher.encrypt(bytes(messageBlock))
		fout.write(cipherText)
		print(bytearray(cipherText))
		print()

	fout.close()

if __name__ == "__main__":
	exit(main())
