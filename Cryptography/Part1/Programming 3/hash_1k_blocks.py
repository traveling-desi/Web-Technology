#!/usr/bin/python
# -* coding: utf-8 -*-

import binascii
import os
from Crypto.Hash import SHA256
from Crypto import Random


target = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"


myfile = "hw.mp4"
block_size = 1024
f_s = os.path.getsize('/Users/sarpotd/Desktop/Coursera_Cryptography/Programming 3/hw.mp4')
f_b = f_s/block_size
l_bytes = f_s - f_b*block_size
f = open(myfile, "rb")
ctr = 0
bytes =[]
try:
	while ctr < f_b:
   		bytes.append((f.read(block_size)))
		ctr = ctr + 1
   	bytes.append((f.read(l_bytes)))
finally:
	f.close()
ctr = f_b + 1
pre_hash = ""
pre_hex_hash = ""
while ctr > 0:
	ctr = ctr - 1
	print "CTR =" + str(ctr)
	h = SHA256.new(bytes[ctr]+pre_hash)
	pre_hash = h.digest()
	pre_hex_hash = h.hexdigest()
	print pre_hex_hash
	print "===================================================="
