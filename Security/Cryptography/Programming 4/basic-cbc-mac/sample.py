from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

Oracle_Connect()

tag = Mac(data, len(data))

ret = Vrfy(data, 0, tag)

if (ret):
    print "Message verified successfully!"
else:
    print "Message verification failed."

Oracle_Disconnect()
