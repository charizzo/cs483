#!/usr/bin/env python3
from sys import argv, exit
from random import randrange, getrandbits
from Crypto.Util import number
import math
import random
import sys


def main():
	smallprime=[3,5,7,11,13,17,19,23,29]
	trash=sys.argv[1];
	if trash != "-p":
		print("error wrong 1st argument")
	pubkey=sys.argv[2];
	trash=sys.argv[3];
	if trash != "-s":
		print("error wrong 2nd argument")
	privkey=sys.argv[4];
	trash=sys.argv[5];
	if trash != "-n":
		print("error wrong 3rd argument")
	N=sys.argv[6];
	N=int(N)
	p=bigoleprime(N)
	check=isprime(p,N)
	while(True):
		p=bigoleprime(N)
		check=isprime(p,N)
		if check:
			break
	print("P {}".format(p))
	q=bigoleprime(N)
	check=isprime(q,N)
	while(True):
		q=bigoleprime(N)
		check=isprime(q,N)
		if check:
			break
	print("q {}".format(q))
	phiN=(p-1)*(q-1)
	print("phi N = {}" .format(phiN))
	for i in smallprime:
		e=math.gcd(i,phiN)
		if(e==1):
			e=i
			print("e = {}" .format(e))
			break
	d = inverse(e, phiN)
	print("d = {} ".format(d))
	puk=open(pubkey,"w")
	puk.write(str(N)+"\n")
	puk.write(str(phiN)+"\n")
	puk.write(str(e)+"\n")
#	puk.close()
	prik=open(privkey,"w")
	prik.write(str(N)+"\n")
	prik.write(str(phiN)+"\n")
	prik.write(str(d)+"\n")


def inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa  
    return lx

def isprime(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def bigoleprime(length):
#	primeNum = number.getPrime(int(n_length))
#	return primeNum
	p = getrandbits(length)
	p |= (1 << length - 1) | 1
	return p

if __name__ == "__main__":
	exit(main())
