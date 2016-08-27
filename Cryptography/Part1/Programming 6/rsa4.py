import numpy as np
import math
import scipy as sp
import gmpy2
from gmpy2 import mpz
from gmpy2 import mpfr


gmpy2.get_context().precision = 200
#print gmpy2.get_context()



N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581


p = 13407807929942597099574024998205846127479365820592393377723561443721764030073662768891111614362326998675040546094339320838419523375986027530441562135724301

cipher = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540

q = gmpy2.div(N,p)
print q
print "Original N"
print N
print "Mulitplication"
print gmpy2.mpz(p*q)
if gmpy2.is_prime(p):
	print "P is prime"
if gmpy2.is_prime(q):
	print "q is prime"

one = gmpy2.mpz(1)
p_1 = p - 1
q_1 = q - 1


print "P -1"
print p_1
print "Q -1"
print q_1

tot_N = p_1 * q_1
print tot_N

e = 65537
print e
d = gmpy2.divm(one,e,tot_N)
print d
print (d*e)%tot_N

plain_dec = gmpy2.powmod(cipher,d,N)
print plain_dec.digits(16)

