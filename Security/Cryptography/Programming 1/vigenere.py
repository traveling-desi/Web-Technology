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


#cText = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA147"
cText = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"


cLen = len(cText)/2


#print cLen
#print cAdd

dict = { '' : 0.0 };

for kLength in range (1, 14):
	cAdd = float(1.0 * kLength/cLen)
	for y in range(0, kLength):
	#for y in range(0, 1):
		dict.clear();
		print "kLength =" + str(kLength)
		#print "Y =" 
		#print y
		for x in range(y*2, cLen*2, kLength*2):
			#print x
			text = "".join([cText[x],cText[x+1]])
			#print text
			if dict.has_key(text):
				dict[text] += cAdd
				#dict[text] += 1
			else:
				dict[text] = cAdd
				#dict[text] = 1
		#print dict.items()

		qDist = 0.0
		for key in dict.keys():
			qDist += pow(dict[key],2)
		print qDist
		#print len(dict)


print "cLen = " + str(cLen) 
for kLength in range (7, 8):
	print "kLength =" + str(kLength)
	for y in range(0, kLength):
	#for y in range(0, 1):
		print "Y =" + str(y)
		numbytes = 0
		max_found = 0
		max_byteB = 0
		for byteB in range (0, 255):
			#print "BB =" + str(byteB)
			notGood = 0
			found = 0
			for x in range(y*2, cLen*2, kLength*2):
				#print "x =" + str(x)

				text = "".join([cText[x],cText[x+1]])
				textH = (int(text,16))
				textCheck = (textH ^ byteB)
				#print textH
				#print (textH ^ byteB)
				if( textCheck > 127 or textCheck < 32 ):
					#print "here"
					#print "ByteB = " + str(byteB)
					notGood = 1
					break
				else:
					if (textCheck == 101 or textCheck == 116 or textCheck == 97 or textCheck == 104 or textCheck == 110 or textCheck == 105):
						found += 1
 			if (notGood != 1):
				if (found > max_found):
					max_found = found
					max_byteB = byteB
 				notGood = 0			
				numbytes += 1
		print "numbytes =" + str(numbytes)
		print "byteB =" + str(max_byteB)


k1 = ["\xaf", "\xbc", "\xbd"] 
k2 = ["\x0e", "\x08"]
k3 = ["\x80", "\x83", "\x8a", "\x90"]
k4 = ["\xa8", "\xa9", "\xab", "\xb2", "\xb6"]
k5 = ["\x1a", "\x42", "\x44", "\x53", "\x54", "\x55", "\x59", "\x5f"]
k6 = ["\xc1", "\xc6", "\xc7", "\xcc", "\xd0", "\xdd"]
k7 = ["\x25", "\x2b", "\x2e", "\x33", "\x38", "\x39", "\x3e"]


k1 = ["\xbc", "\xbd"] 
k2 = ["\x0e"]
k3 = ["\x80", "\x83", "\x8a", "\x90"]
k4 = ["\xa8", "\xa9", "\xab", "\xb2", "\xb6"]
k5 = ["\x1a", "\x44", "\x53", "\x54", "\x55", "\x59", "\x5f"]
k6 = ["\xc1", "\xc6", "\xc7", "\xcc", "\xd0", "\xdd"]
k7 = ["\x25", "\x2b", "\x2e", "\x33", "\x38", "\x39", "\x3e"]

for a in k1:
	for b in k2:
		for c in k3:
			for d in k4:
				for e in k5:
					for f in k5:
						for g in k5:
							#key = (a+b+c+d+e+f+g)*134
							key = "\xba\x1f\x91\xb2\x53\xcd\x3e" * 134 
							key = key + "\xba"
							#print key.encode('hex')
							prt_string = strxor(cText.decode('hex'), key)
						
print prt_string
