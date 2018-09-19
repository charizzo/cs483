#!/usr/bin/env python3

from sys import argv, exit
from Crypto.Cipher import AES 
from Crypto import Random
import os.path
import sys

def main():
	if len(argv) != 7:
		print("Usage: ./cbcmac-tag.py -k <key file> -m <message file> -t <tag file>")
		raise Exception("Bad Command Line Args")	
	fin = open(argv[2],"r")
	hexKey = fin.read().strip()
	fin.close()
	
	fout = open(argv[6],"wb+")
	
	blockCipher = AES.new(bytes.fromhex(hexKey),AES.MODE_ECB)
	
	fin = open(argv[4],"rb")
	msgToTag = fin.read().strip()
	msgSize = len(msgToTag)
	fin.close()
	
	fin = open(argv[4],"rb")
	strmsg=format(msgSize,'0128b')
	prevBlock = bytearray(blockCipher.encrypt(strmsg))
	
	while 1:
		msgToTag = bytearray(fin.read(16).strip())
		if(len(msgToTag) != 16 and msgToTag != bytes('','utf-8')):
			padding = 16 - len(msgToTag)
			for i in range(0,padding):
				msgToTag += padding.to_bytes(1,byteorder='big')
		
		if msgToTag == bytes('','utf-8'):
			break
		for i in range(0,16):
			msgToTag[i] ^= prevBlock[i]
		prevBlock = bytearray(blockCipher.encrypt(bytes(msgToTag)))
	
	fin.close()
	fout.write(prevBlock)
	fout.close()

if __name__ == "__main__":
	exit(main())

