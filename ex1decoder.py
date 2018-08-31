#!/usr/bin/env python3

from sys import argv, exit

def main():
	if len(argv) != 3:
		print("Usage: ./ex1decoder.py encodedFile freqFile")
		raise Exception("Bad Arguments")
	
	fin = open(argv[1], "r")
	text = fin.read().strip()
	fin.close()

	fin = open(argv[2], "r")
	frequencies = {}
	while 1:
		freqLine = fin.readline().strip()
		if freqLine == '':
			break
		line = freqLine.split(",")
		frequencies[line[0]] = line[1]

	correctKey = shift_cipher(frequencies, text)
	print("\nThe correct key is %d" %(correctKey))
	return 0

def shift_cipher(frequencies, encodedText):
	decodedText = ''
	decryptedFreqs = {}
	currentMin = 100000
	target = 0.066
	savedKey = -1
	for i in range(0,26):
		for letter in list(frequencies.keys()):
			decryptedFreqs[letter] = 0
		for j in encodedText:
			char = ord(j) - i
			if char < 97:
				char += 26
			
			decryptedFreqs[chr(char)] = 1 + decryptedFreqs[chr(char)]
			decodedText += chr(char)
		
		sOs = calculateFrequencies(frequencies,decryptedFreqs, len(encodedText))
		
		if abs(sOs - target) < currentMin:
			writeDecodedToFile(decodedText)
			savedKey = i
			currentMin = abs(sOs - target)
		print("Key %d yields differential %f" %(i, abs(sOs - target)))
		decodedText = ''
	
	return savedKey

def calculateFrequencies(frequencies, decryptedFreqs, length):
	freqs = list(frequencies.values())
	dFreqs = list(decryptedFreqs.values())
	
	sumOfSquares = 0
	for i in range(0, len(freqs)):
		sumOfSquares += float(freqs[i]) * (float(dFreqs[i]) / length)

	return sumOfSquares
def vigenere_cipher(frequencies,encodedText):
	decryptedfreq={}
	target = .066
	j=0
	for i in range(0,len(encodedText)):
		for letter in list(frequencies.keys())
			decryptedfreq[letter]=0
		decryptedfreq[char(encodedText[i+j]]



		









def writeDecodedToFile(text):
	fout = open("decodedOutput.txt", "w")
	fout.write(text)
	fout.close()

if __name__ == "__main__":
	exit(main())
