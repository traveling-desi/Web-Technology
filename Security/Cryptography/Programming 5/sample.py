from oracle import *
from helper import *

n = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869

e = 65537

Oracle_Connect()

msg = "Crypto is hard --- even schemes that look complex can be broken"
#msg = "Crypto is hard --- even schemes that look complex can be broke."

#MSG = "00"+ascii_to_hex(msg)+"00"+ascii_to_hex(msg)
#print MSG

m = ascii_to_int(msg)
#print m

temp = pow(2,504) - 1
#temp = pow(2,64) - 1
print "temp = ",
print temp


# Should fail, because you're not allowed to query on the original message
sigma = Sign(m)
print "Org sigma = ",
print sigma
#assert(sigma < 0)

# All other arbitrary messages <= 504 bits should be accepted by the oracle
#msg = "Hello, World!"
#m = ascii_to_int(msg)



m1 = 1
print m1

sigma1 = Sign(m1)
print "sigma1 = ",
print sigma1

sigma1_inv = modinv(sigma1,n)


#K = 1 << 512 + 1
#K_inv = modinv(2,n)
K_inv = 0.5
print "K_inv = ",
print K_inv

m2 = m/2
print "m2 = ",
print m2

sigma2 = Sign(m2)
print "sigma2 = ",
print sigma2

m3 = 2
sigma3 = Sign(m3)
print "sigma3 = ",
print sigma3

new_sigma =  ( sigma1_inv * sigma2 * sigma3 ) %n
print "sigma = ",
print new_sigma

#new_m = pow(new_sigma, e, n)
print "Org sigma = ",
print sigma
print "New sigma = ",
print hex(new_sigma)


if sigma < 0:
    raise SystemExit

if Verify(m,sigma):
    print "Oracle is working properly!"

Oracle_Disconnect()
