import numpy as np
import math
import scipy as sp
import gmpy2
from gmpy2 import mpz
from gmpy2 import mpfr


N = gmpy2.mpz(648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877)

gmpy2.get_context().precision = 200
#print gmpy2.get_context()


sqrt_N = gmpy2.mpz(gmpy2.isqrt(N))

i = 1
while i < (pow(2,20)):
	A = gmpy2.mpz(sqrt_N + i)
	x = gmpy2.isqrt(gmpy2.mpz(pow(A,2)) - N)
	p = gmpy2.mpz(A - x)
	if gmpy2.is_prime(p):
		q = gmpy2.mpz(N/p)
		if gmpy2.is_prime(q):
			print "p ="
			print p
			print "q ="
			print q
			if (p > q):
				print "Bigger is p"
			else:
				print "Bigger is q"
			print "Original N"
			print N
			print "Mulitplication"
			print gmpy2.mpz(p*q)
			break
	i = i+1
