#!/usr/bin/env python3

from sys import argv,exit
from Crypto.Cipher import AES
from Crypto import Random
from multiprocessing import Pool
import os.path

def main():
	if len(argv) != 7:
		print("Usage: ./ctr-enc.py -k <key file> -i <input file> -o <output file>")
		raise Exception("Bad Command Line Args")

	fin = open(argv[2],"r")
	hexKey = fin.read().strip()
	fin.close()

	fout = open(argv[6],"wb+")


	counter = 0
	messageBlocks = []
	fin = open(argv[4],"rb")
	while 1:
		temp = bytearray(fin.read(16)) #Getting rid of strip like with cbc
		if temp == bytes('','utf-8'):
			break
		messageBlocks.append(temp)
		counter += 1
	fin.close()	

	IV = os.urandom(16)
	bitch=int.from_bytes(IV,byteorder='big')
	cipher = AES.new(bytes.fromhex(hexKey),AES.MODE_ECB)
	fout.write(IV)

	for i in range (0,counter):
		strmsg=format(bitch,'0128b')
		interMed = bytearray(cipher.encrypt(strmsg))
		print(interMed)
		for j in range (0,len(messageBlocks[i])):
			print()
			interMed[i] ^=	messageBlocks[i][j]
		fout.write(interMed)
		bitch+=1

	fout.close()
#	with Pool(4) as p:
#		cipherTexts = [[p.apply(encrypt,args=(x,y,hexKey)) for x in messageBlocks] for y in range(int.from_bytes(IV,byteorder='big')+1,int.from_bytes(IV,byteorder='big') + len(messageBlocks) + 1)]


#def encrypt(msg,IV,hexKey):
#	cipher = AES.new(bytes.fromhex(hexKey),AES.MODE_ECB)
#	interMed = bytearray(cipher.encrypt(bytes(IV)))
#	for i in range (0,16):
#		msg[i] ^= interMed[i]
#	return msg	
	


if __name__ == "__main__":
	exit(main())
