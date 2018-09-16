#!/usr/bin/env python3

from sys import argv,exit
from Crypto.Cipher import AES

def main():
	if len(argv) != 7:
		print("Usage: ./cbc-enc.py -k <key file> -i <input file> -o <output file>")
		raise Exception("Bad Command Line Args")

	




if __name__ == "__main__":
	exit(main())
