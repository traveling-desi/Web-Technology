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

ciphertext1 = "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e"

ciphertext2 = "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f"

ciphertext3 = "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb"

ciphertext4= "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa"

ciphertext5= "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070"

ciphertext6= "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4"

ciphertext7= "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce"

ciphertext8= "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3"

ciphertext9= "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027"

ciphertext10= "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83"

target_ciphertext = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"

max_len = max(len(ciphertext1), len(ciphertext2), len(ciphertext3), len(ciphertext4), len(ciphertext5), len(ciphertext6), len(ciphertext7), len(ciphertext8), len(ciphertext9), len(ciphertext10))



ciphertext1_padded = pad_bits_append(ciphertext1,max_len)
ciphertext2_padded = pad_bits_append(ciphertext2,max_len)
ciphertext3_padded = pad_bits_append(ciphertext3,max_len)
ciphertext4_padded = pad_bits_append(ciphertext4,max_len)
ciphertext5_padded = pad_bits_append(ciphertext5,max_len)
ciphertext6_padded = pad_bits_append(ciphertext6,max_len)
ciphertext7_padded = pad_bits_append(ciphertext7,max_len)
ciphertext8_padded = pad_bits_append(ciphertext8,max_len)
ciphertext9_padded = pad_bits_append(ciphertext9,max_len)
ciphertext10_padded = pad_bits_append(ciphertext10,max_len)
target_ciphertext_padded = pad_bits_append(target_ciphertext,max_len)

#print ciphertext1_padded
#print ciphertext8_padded


new_cipher12 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext2_padded, 16)), max_len)
new_cipher13 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext3_padded, 16)), max_len)
new_cipher14 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext4_padded, 16)), max_len)
new_cipher15 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext5_padded, 16)), max_len)
new_cipher16 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext6_padded, 16)), max_len)
new_cipher17 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext7_padded, 16)), max_len)
new_cipher18 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher19 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher110 = pad_bits_append( '%x' %(int(ciphertext1_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher23 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext3_padded, 16)), max_len)
new_cipher24 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext4_padded, 16)), max_len)
new_cipher25 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext5_padded, 16)), max_len)
new_cipher26 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext6_padded, 16)), max_len)
new_cipher27 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext7_padded, 16)), max_len)
new_cipher28 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher29 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher210 = pad_bits_append( '%x' %(int(ciphertext2_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher34 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext4_padded, 16)), max_len)
new_cipher35 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext5_padded, 16)), max_len)
new_cipher36 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext6_padded, 16)), max_len)
new_cipher37 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext7_padded, 16)), max_len)
new_cipher38 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher39 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher310 = pad_bits_append( '%x' %(int(ciphertext3_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher45 = pad_bits_append( '%x' %(int(ciphertext4_padded, 16) ^ int(ciphertext5_padded, 16)), max_len)
new_cipher46 = pad_bits_append( '%x' %(int(ciphertext4_padded, 16) ^ int(ciphertext6_padded, 16)), max_len)
new_cipher47 = pad_bits_append( '%x' %(int(ciphertext4_padded, 16) ^ int(ciphertext7_padded, 16)), max_len)
new_cipher48 = pad_bits_append( '%x' %(int(ciphertext4_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher49 = pad_bits_append( '%x' %(int(ciphertext4_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher410 = pad_bits_append( '%x' %(int(ciphertext4_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher56 = pad_bits_append( '%x' %(int(ciphertext5_padded, 16) ^ int(ciphertext6_padded, 16)), max_len)
new_cipher57 = pad_bits_append( '%x' %(int(ciphertext5_padded, 16) ^ int(ciphertext7_padded, 16)), max_len)
new_cipher58 = pad_bits_append( '%x' %(int(ciphertext5_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher59 = pad_bits_append( '%x' %(int(ciphertext5_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher510 = pad_bits_append( '%x' %(int(ciphertext5_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher67 = pad_bits_append( '%x' %(int(ciphertext6_padded, 16) ^ int(ciphertext7_padded, 16)), max_len)
new_cipher68 = pad_bits_append( '%x' %(int(ciphertext6_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher69 = pad_bits_append( '%x' %(int(ciphertext6_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher610 = pad_bits_append( '%x' %(int(ciphertext6_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher78 = pad_bits_append( '%x' %(int(ciphertext7_padded, 16) ^ int(ciphertext8_padded, 16)), max_len)
new_cipher79 = pad_bits_append( '%x' %(int(ciphertext7_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher710 = pad_bits_append( '%x' %(int(ciphertext7_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher89 = pad_bits_append( '%x' %(int(ciphertext8_padded, 16) ^ int(ciphertext9_padded, 16)), max_len)
new_cipher810 = pad_bits_append( '%x' %(int(ciphertext8_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

new_cipher910 = pad_bits_append( '%x' %(int(ciphertext9_padded, 16) ^ int(ciphertext10_padded, 16)), max_len)

#print "STRING12 =" + str( new_cipher12.decode('hex'))
##print "STRING12 =" + new_cipher12.decode('hex')
##print "STRING13 =" + str( new_cipher13.decode('hex'))
##print "STRING14 =" + str( new_cipher14.decode('hex'))
##print "STRING15 =" + str( new_cipher15.decode('hex'))
##print "STRING16 =" + str( new_cipher16.decode('hex'))
##print "STRING17 =" + str( new_cipher17.decode('hex'))
##print "STRING18 =" + str( new_cipher18.decode('hex'))
##print "STRING19 =" + str( new_cipher19.decode('hex'))
##print "STRING110 =" + str( new_cipher110.decode('hex'))
##
##print "STRING23 =" + str( new_cipher23.decode('hex'))
##print "STRING24 =" + str( new_cipher24.decode('hex'))
##print "STRING25 =" + str( new_cipher25.decode('hex'))
##print "STRING26 =" + str( new_cipher26.decode('hex'))
##print "STRING27 =" + str( new_cipher27.decode('hex'))
##print "STRING28 =" + str( new_cipher28.decode('hex'))
##print "STRING29 =" + str( new_cipher29.decode('hex'))
##print "STRING210 =" + str( new_cipher210.decode('hex'))
##
##print "STRING34 =" + str( new_cipher34.decode('hex'))
##print "STRING35 =" + str( new_cipher35.decode('hex'))
##print "STRING36 =" + str( new_cipher36.decode('hex'))
##print "STRING37 =" + str( new_cipher37.decode('hex'))
##print "STRING38 =" + str( new_cipher38.decode('hex'))
##print "STRING39 =" + str( new_cipher39.decode('hex'))
##print "STRING310 =" + str( new_cipher310.decode('hex'))
##
##print "STRING45 =" + str( new_cipher45.decode('hex'))
##print "STRING46 =" + str( new_cipher46.decode('hex'))
##print "STRING47 =" + str( new_cipher47.decode('hex'))
##print "STRING48 =" + str( new_cipher48.decode('hex'))
##print "STRING49 =" + str( new_cipher49.decode('hex'))
##print "STRING410 =" + str( new_cipher410.decode('hex'))
##
##print "STRING56 =" + str( new_cipher56.decode('hex'))
##print "STRING57 =" + str( new_cipher57.decode('hex'))
##print "STRING58 =" + str( new_cipher58.decode('hex'))
##print "STRING59 =" + str( new_cipher59.decode('hex'))
##print "STRING510 =" + str( new_cipher510.decode('hex'))
##
##print "STRING67 =" + str( new_cipher67.decode('hex'))
##print "STRING68 =" + str( new_cipher68.decode('hex'))
##print "STRING69 =" + str( new_cipher69.decode('hex'))
##print "STRING610 =" + str( new_cipher610.decode('hex'))
##
##print "STRING78 =" + str( new_cipher78.decode('hex'))
##print "STRING79 =" + str( new_cipher79.decode('hex'))
##print "STRING710 =" + str( new_cipher710.decode('hex'))
##
##print "STRING89 =" + str( new_cipher79.decode('hex'))
##print "STRING810 =" + str( new_cipher810.decode('hex'))
##
##print "STRING910 =" + str( new_cipher910.decode('hex'))









##
##print " "
##print new_cipher12
##print " "
##print new_cipher13
##print " "
##print new_cipher14
##print " "
##print new_cipher15
##print " "
##print new_cipher16
##print " "
##print new_cipher17
##print " "
##print new_cipher18
##print " "
##print new_cipher19
##print " "
##print new_cipher110
##print " "
##print new_cipher23
##print " "
##print new_cipher45
##print " "
##print new_cipher67
##print " "
##print new_cipher89
##print " "
##
##
####space_text = "20" * (max_len/2)
####
####print "new"
####
####new_cipher12_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher12, 16)), max_len)
####new_cipher13_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher13, 16)), max_len)
####new_cipher14_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher14, 16)), max_len)
####new_cipher15_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher15, 16)), max_len)
####new_cipher16_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher16, 16)), max_len)
####new_cipher17_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher17, 16)), max_len)
####new_cipher18_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher18, 16)), max_len)
####new_cipher19_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher19, 16)), max_len)
####new_cipher110_space = pad_bits_append( '%x' %(int(space_text, 16) ^ int(new_cipher110, 16)), max_len)
####
####
####print " "
####print new_cipher12_space
####print " "
####print new_cipher13_space
####print " "
####print new_cipher14_space
####print " "
####print new_cipher15_space
####print " "
####print new_cipher16_space
####print " "
####print new_cipher17_space
####print " "
####print new_cipher18_space
####print " "
####print new_cipher19_space
####print " "
####print new_cipher110_space
####print " "


allcrypthex = (ciphertext1_padded.decode('hex'), ciphertext2_padded.decode('hex'), ciphertext3_padded.decode('hex'), ciphertext4_padded.decode('hex'), ciphertext5_padded.decode('hex'), ciphertext6_padded.decode('hex'), ciphertext7_padded.decode('hex'), ciphertext8_padded.decode('hex'), ciphertext9_padded.decode('hex'), ciphertext10_padded.decode('hex'),target_ciphertext_padded.decode('hex'))

solution = "f9n\x89\xc9\xdb\xd8\xcc\x98\x74\x35\x2a\xcd\x63\x95\x10\x2e\xaf\xce\x78\xaa\x7f\xed\x28\xa0\x7f\x6b\xc9\x8d\x29\xc5\x0b\x69\xb0\x33\x9a\x19\xf8\xaa\x40\x1a\x9c\x6d\x70\x8f\x80\xc0\x66\xc7\x63\xfe\xf0\x12\x31\x48\xcd\xd8\xe8\x02\xd0\x5b\xa9\x87\x77\x33\x5d\xae\xfc\xec\xd5\x9c\x43\x3a\x6b\x26\x8b\x60\xbf\x4e\xf0"

allcrypt = [strxor(s, solution) for s in allcrypthex]
print allcrypt


next = strxor(chr(int(target_ciphertext_padded[158:160], 16)), 'o')
#next = strxor(chr(int(ciphertext1_padded[140:142], 16)), ' ')
print next
print next.encode('hex')
