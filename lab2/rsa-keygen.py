#!/usr/bin/env python3
from sys import argv, exit
from Crypto.Util import number
import math
import random
import sys


def main():
	smallprime=[3,5,7,11,13,17,19,23,29]
	N=sys.argv[1];
	N=int(N)
	p=bigoleprime(N)
	check=isprime(p,N)
	while(check!=True):
		p=bigoleprime(N)
		check=isprime(p,N)
	print("P {}".format(p))
	q=bigoleprime(N)
	check=isprime(q,N)
	while(check!=True):
		q=bigoleprime(N)
		check=isprime(q,N)
	print("q {}".format(q))
	phiN=(p-1)*(q-1)
	print(phiN)
	phiN=3172
	for i in smallprime:
		e=math.gcd(i,phiN)
		if(e==1):
			e=i
			print(e)
			break
	d=egcd(e,phiN)
	print(d)
			
def egcd(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
def isprime(a,n):
	possible = random.randrange(2**(n-1)+1, 2**n)|1
	return 1 not in ipow(a, possible-1, possible)
def ipow(a,b,n):
    #calculates (a**b)%n via binary exponentiation, yielding itermediate
    #results as Rabin-Miller requires
    A = a = a%n
    yield A
    t = 1
    while t <= b:
        t <<= 1
    
    #t = 2**k, and t > b
    t >>= 2
    
    while t:
        A = (A * A)%n
        if t & b:
            A = (A * a) % n
        yield A
        t >>= 1
def bigoleprime(n_length):

	primeNum = number.getPrime(int(n_length))
	return primeNum


if __name__ == "__main__":
	exit(main())
