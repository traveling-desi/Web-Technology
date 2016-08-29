from oracle import *
import sys
import copy


##### need to remove the last block of text where the padding occurs


if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

cText = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
cTextSaved = copy.copy(cText)
cLen = len(cText)
pText = [0] * cLen
print pText


numBlocks = (cLen/16) - 1    ## Dont need to decode the IV
bLength = 16
padStart = -1

print cText
print cLen

Oracle_Connect()

#rc = Oracle_Send(cText, 3)
#print("Oracle returned: %d " % (rc))

newPadLength = 0

### 11 bits of padding
for blockNum in range (0, numBlocks):
	bStart = (numBlocks-blockNum-1) * 16
	bEnd = bStart + bLength
	print "bStart = " + str(bStart)
	print "bEnd = " + str(bEnd)
	
 	for index1 in range (bEnd-1, bStart-1, -1):
 		cText = copy.copy(cTextSaved)
 		print "index1 = " + str(index1)
		print cText[index1]

             	for index2 in range (index1, bEnd):
                        newPadLength = (bEnd - index1)
			if (index1 == bEnd-1):
				break
                        print ("newPadLength %d added starting @ %d index" % (newPadLength, index2))
                        saveInt = cText[index2]
                        cText[index2] =  cText[index2] ^ pText[index2+bLength] ^ newPadLength 
                        print ("old value was %d, new value is %d" % (saveInt, cText[index2]))

  		for ctr in range (0, 256):
  			cText[index1] = ctr
  			rc = Oracle_Send(cText, 2)
  			#print("Oracle returned: %d for ctr %d" % (rc, ctr))
 			if (rc == 1):
  				print("Oracle returned: %d for ctr %d" % (rc, ctr))
				print ("saveInt is %d" %cTextSaved[index1])
				print ("newPadLength is %d" %newPadLength)
				print ("ctr is %d" %ctr)
 				msgByte = cTextSaved[index1] ^ newPadLength ^ ctr
				pText[index1+bLength] = msgByte
 				print ("Decoded msgbyte is %d" %msgByte)
				break
		print pText

Oracle_Disconnect()
