#!/usr/bin/python
# -* coding: utf-8 -*-

import binascii
from Crypto.Cipher import AES
from Crypto import Random



def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

def pad_bits_append (small, size):
	diff = max(0, size - len(small))
    	return small + "0" * diff

def pad_bits (small, size):
	diff = max(0, size - len(small))
    	return "0" * diff + small


#c_t = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
#c_t = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
#cbc_key = "140b41b22a29beb4061bda66b6747e14"

ctr_key = "36f18357be4dbd77f050515c73fcf9f2"
#c_t = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
c_t = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"

   
iv = c_t[0:32]
print "IV =" + iv
print len(c_t)
ctr = 0



m_s = ""
i = 32
while i < len(c_t):
	c_s = c_t[i:i+32]
	print "CS = " + c_s
	iv = ('%x' %(int(c_t[0:32],16) + ctr))
	print "IV =" + iv
	#obj=AES.new(ctr_key.decode('hex'), AES.MODE_CBC, iv.decode('hex'))
	obj=AES.new(ctr_key.decode('hex'), AES.MODE_ECB)
	d_c_s = obj.encrypt(iv.decode('hex'))
	print "DCS = " + d_c_s.encode('hex')
	m_s = m_s + strxor(c_t[i:i+32].decode('hex'), d_c_s)
	print m_s
	i = i + 32
	ctr = ctr + 1


	
#r_t = Random.get_random_bytes(8)
#obj.encrypt(plain)

#CBC key: 140b41b22a29beb4061bda66b6747e14
#CBC Ciphertext 1: 4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81
#CBC key: 140b41b22a29beb4061bda66b6747e14
#CBC Ciphertext 2: 5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253
#CTR key: 36f18357be4dbd77f050515c73fcf9f2
#CTR Ciphertext 1: 69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329
#CTR key: 36f18357be4dbd77f050515c73fcf9f2
#CTR Ciphertext 2: 770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451
