import numpy as np
import math
import scipy as sp
import gmpy2
from gmpy2 import mpz


N = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929


gmpy2.get_context().precision = 1400
#print gmpy2.get_context()

N_24 = gmpy2.mul(N,24)
(A_temp,A_temp_rem) = gmpy2.isqrt_rem(N_24)
A_two = A_temp + 1
print A_temp_rem
print gmpy2.mul(A_two,A_two) - N_24
(x,x_rem) = gmpy2.isqrt_rem(gmpy2.mul(A_two,A_two) - N_24)
(p,p_rem) = gmpy2.f_divmod(A_two+x,4)
(q,q_rem) = gmpy2.f_divmod(A_two-x,6)
print gmpy2.is_prime(p)
print gmpy2.is_prime(q)
print q

