from oracle import *
import sys
import binascii


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

data = data.rstrip()
data_0_32 = data[0:32]
data_32_48 = data[32:48]
data_48_64 = data[48:64]

#print len(data)
#for i in range (0,len(data)):
#	print ("%d, %s" %(i,data[i]))
#print "test"

#print data
#print data_0_32
#print data_48_64
#print len(data.encode('hex'))
#print len(data_0_32.encode('hex'))
#print len(data_48_64.encode('hex'))


Oracle_Connect()

tag_0_32 = Mac(data_0_32, len(data_0_32))
tag_0_32_hex = binascii.hexlify(bytearray(tag_0_32))

#print tag_0_32_hex
#print tag_0_32_hex.decode('hex')
#print data_32_48.encode('hex')
#print data_32_48
#print strxor(tag_0_32_hex, data_32_48.encode('hex'))

data_new_32_48 = strxor(tag_0_32_hex.decode('hex'), data_32_48)
#print strxor(tag_0_32_hex.decode('hex'), data_32_48)
data_new_0_64 = data_new_32_48 + data_48_64

#print tag_0_32.encode('hex')
#print tag_32_64.encode('hex')

tag_new_0_64 = Mac(data_new_0_64, len(data_new_0_64))

print "Required Tag is = " + binascii.hexlify(bytearray(tag_new_0_64))

ret_0_32 = Vrfy(data_0_32, 32, tag_0_32)
ret_new_0_64 = Vrfy(data_new_0_64, 32, tag_new_0_64)
ret_0_64 = Vrfy(data, 64, tag_new_0_64)

#print ret_0_64
#print ret_new_0_64
#print ret_0_32

if (ret_0_64 == 1):
    print "Message verified successfully!"
else:
    print "Message verification failed."


Oracle_Disconnect()
