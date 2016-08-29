#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import binascii

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




ciphertext1 = "BB4A65F6F0034FA957F6A767699CE7FABA855AFB4F2B520AEAD612944A801E"
ciphertext2 = "BA7F24F2A35357A05CB8A16762C5A6AAAC924AE6447F0608A3D11388569A1E"
ciphertext3 = "A67261BBB30651BA5CF6BA297ED0E7B4E9894AA95E300247F0C0028F409A1E"
ciphertext4 = "A57261F5F0004BA74CF4AA2979D9A6B7AC854DA95E305203EC8515954C9D0F"
ciphertext5 = "BB3A70F3B91D48E84DF0AB702ECFEEB5BC8C5DA94C301E0BECD241954C831E"
ciphertext6 = "A6726DE8F01A50E849EDBC6C7C9CF2B2A88E19FD423E0647ECCB04DD4C9D1E"
ciphertext7 = "BC7570BBBF1D46E85AF9AA6C7A9CEFA9E9825CFD5E3A0047F7CD009305A71E"


new_cipher12 = ( '%x' %(int(ciphertext1, 16) ^ int(ciphertext2, 16)) )

allcrypthex = ( ciphertext1.decode('hex'), ciphertext2.decode('hex'), ciphertext3.decode('hex'), ciphertext4.decode('hex'), ciphertext5.decode('hex'), ciphertext6.decode('hex'), ciphertext7.decode('hex') )
#allcrypthex = ( ciphertext1.decode('hex'), ciphertext2.decode('hex'), ciphertext3.decode('hex') )

#solution = "\x20\x20\x61\x20\x73\x70\x38\x20\x20\x6e\x20\x20\x20\x79\x61\x70\x36\x37\x30\x20\x20\x74\x74\x20\x69\x20\x20\x20\x20\x20\x30"
solution = "\xd2\x1a\x04\x9b\xd0\x73\x23\xc8\x39\x98\xce\x09\x0e\xbc\x86\xda\xc9\xe0\x39\x89\x2a\x5f\x72\x67\x83\xa5\x61\xfd\x25\xee\x30"

#allcrypt = [strxor(s, solution) for s in allcrypthex]
#allcrypt2 = [strxor(s, solution) for s in allcrypt]
allcrypt = [strxor(s, ciphertext1.decode('hex')) for s in allcrypthex]
allcrypt2 = [strxor(s, solution) for s in allcrypt]
allcrypt3 = [strxor(s, solution) for s in allcrypthex]
print "m1 xor m2 = [" 
print allcrypt
print "m1 xor m2 xor solution = [" 
print allcrypt2
print "c1 xor solution = [" 
print allcrypt3
