#!/usr/bin/env python3

from sys import argv, exit
from itertools import combinations_with_replacement

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
			writeDecodedToFile(decodedText)
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
		
	keyFind(savedPeriod,encodedText, frequencies)
		
def keyFind(period,encodedText, frequencies):
	nums = [0] * 26
	decryptedCharCount = {}
	target = 0.066
	currentMin = 100000
	savedKey = []

	for i in range (0,26):
		nums[i] = i
	comb = combinations_with_replacement(nums, period)

	for key in list(comb):
		for letter in list(frequencies.keys()):
			decryptedCharCount[letter] = 0 
		for i in range (0,112):
			char = ord(encodedText[i]) - key[i % period]
			if char < 97:
				char += 26
			decryptedCharCount[chr(char)] = 1 + decryptedCharCount[chr(char)]
		
		sOs = calculateFrequencies(frequencies,decryptedCharCount,112)
		
		if abs(sOs - target) < currentMin:
			savedKey = key
			currentMin = abs(sOs - target)
			print("New Min Found: %f" %(currentMin))
			print(savedKey)

	
#	print(savedKey)	
	for j in savedKey:
#		num =  - j
#		if num < 97:
#			num += 26
		print(chr(97 + j))

	return savedKey
			

def calculateFrequencies(frequencies, decryptedFreqs, length):
	freqs = list(frequencies.values())
	dFreqs = list(decryptedFreqs.values())
	
	sumOfSquares = 0
	for i in range(0, len(freqs)):
		sumOfSquares += float(freqs[i]) * (float(dFreqs[i]) / length)

	return sumOfSquares

def writeDecodedToFile(text):
	fout = open("decodedOutput.txt", "w")
	fout.write(text)
	fout.close()

if __name__ == "__main__":
	exit(main())
