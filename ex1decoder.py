#!/usr/bin/env python3

from sys import argv, exit

def main():
	if len(argv) != 4:
		print("Usage: ./ex1decoder.py encodedFile freqFile cipher(vig/shift)")
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

	if argv[3] == "shift":
		correctKey = shift_cipher(frequencies, text, len(text))
		print("\nThe correct key is %d" %(correctKey))
	elif argv[3] == "vig":
		vig_cipher(frequencies,text)

	return 0

def shift_cipher(frequencies, encodedText, lengthOfText):
	decodedText = ''
	decryptedFreqs = {}
	currentMin = 100000
	target = 0.066
	savedKey = -1
	for i in range(0,26):
		for letter in list(frequencies.keys()):
			decryptedFreqs[letter] = 0
		for j in range(0,lengthOfText):
			char = ord(encodedText[j]) - i
			if char < 97:
				char += 26
			
			decryptedFreqs[chr(char)] = 1 + decryptedFreqs[chr(char)]
			decodedText += chr(char)
		
		sOs = calculateFrequencies(frequencies,decryptedFreqs, lengthOfText)
		
		if abs(sOs - target) < currentMin:
			writeDecodedToFile(decodedText,"shiftCipherOutput.txt")
			savedKey = i
			currentMin = abs(sOs - target)
		print("Key %d yields differential %f" %(i, abs(sOs - target)))
		decodedText = ''
	
	return savedKey

def vig_cipher(frequencies, encodedText):
	firstLetterDict = {}
	minDifferential = 100000
	savedPeriod = -1
	target = 0.066
	decryptedCharCount = {}
	amountOfLetters = 0

	for i in range(2,11):
		for letter in list(frequencies.keys()):
			firstLetterDict[letter] = 0
		amountOfLetters = 0
		for j in range(0,len(encodedText),i):
			firstLetterDict[encodedText[j]] += 1;
			amountOfLetters += 1
		
		sOs = calculateFrequencies(frequencies, firstLetterDict,amountOfLetters)		
		
		if abs(sOs - target) < minDifferential:
			savedPeriod = i
			minDifferential = abs(sOs - target)

	key = [''] * savedPeriod

	for i in range(0,savedPeriod):
		minDifferential = 100000
		for j in range(0,26):
			for letter in list(frequencies.keys()):
				decryptedCharCount[letter] = 0
			amountOfLetters = 0
			for k in range(i,len(encodedText),savedPeriod):
				char = ord(encodedText[k]) - j
				if char < 97:
					char += 26
				decryptedCharCount[chr(char)] = 1 + decryptedCharCount[chr(char)]
				amountOfLetters += 1
			
			sOs = calculateFrequencies(frequencies, decryptedCharCount, amountOfLetters) 
			
			if abs(sOs - target) < minDifferential:
				key[i] = chr(j)
				minDifferential = abs(sOs - target)
	
	decodedText = ''
	for i in range(0,len(encodedText)):
		char = ord(encodedText[i]) - (ord(key[i % savedPeriod]))
		if char < 97:
			char += 26
		decodedText += chr(char)

	writeDecodedToFile(decodedText,"vigCipherOutput.txt")

def calculateFrequencies(frequencies, decryptedFreqs, length):
	freqs = list(frequencies.values())
	dFreqs = list(decryptedFreqs.values())
	
	sumOfSquares = 0
	for i in range(0, len(freqs)):
		sumOfSquares += float(freqs[i]) * (float(dFreqs[i]) / length)

	return sumOfSquares

def writeDecodedToFile(text, filename):
	fout = open(filename, "w")
	fout.write(text)
	fout.close()

if __name__ == "__main__":
	exit(main())
