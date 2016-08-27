
import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

if __name__ == "__main__":
    po = PaddingOracle()


iv =  "f20bdba6ff29eed7b046d1df9fb70000"
c_0 = "58b1ffb4210a580f748b4ac714c001bd"
c_1 = "4a61044426fb515dad3f21f18aa577c0"
c_2 = "bdf302936266926ff37dbf7035d5eeb4"


#target2 ="20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d"
#print iv+c_0+c_1+c_2
##saved_c_2 = ""
##j = 31
##while j > 0:
##	prefix = (j-1)/2
##	suffix = (33 - j)/2
##	#print j
##	temp = c_1[:j-1] + ("00"* suffix)
##	pad_str = "00" * prefix + '%0.2x' %suffix * suffix
##	print "Changed C_1 =" + temp
##	print "C_1 prefix1=" + str(prefix)
##	print "C_1 suffix =" + str(suffix)
##	print "PAD_Str C_1 =" +  pad_str
##	for i in range(0,256):
##		y = '%0.2x' %i
##		atk_str = "00" * prefix + y + saved_c_2
##		print "ATK_STR C_1 =" + atk_str
##		print "I =" + str(i)
##		new_c_1 = '%32x' %(int(c_1,16) ^ int(pad_str,16) ^ int(atk_str,16))
##		#new_c_1 = '%32x' %(int(temp,16) ^ int(pad_str,16) ^ int(atk_str,16))
##		print "NEW     C_1 =" +  new_c_1
##		print "CIPHER      =" + iv+c_0+new_c_1+c_2
##		flag = po.query(iv+c_0+new_c_1+c_2)       # Issue HTTP query with the given argument
##		if flag:
##			saved_c_2 = y + saved_c_2
##			print "  SAVED_C_2 =" + saved_c_2
##			break
##	j = j-2
saved_c_1 = ""
j = 31
while j > 0:
	prefix = (j-1)/2
	suffix = (33 - j)/2
	#print j
	temp = c_0[:j-1] + ("00"* suffix)
	print "Changed C_0 =" + temp
	for i in range(0,256):
		y = '%0.2x' %i
		pad_str = "00" * prefix + '%0.2x' %suffix * suffix
		atk_str = "00" * prefix + y + saved_c_1
		print "Pad_str C_0 =" + pad_str
		print "ATK_str C_0 =" + atk_str
		#print int(pad_str,16)
		#print int(atk_str,16)
		new_c_0 = '%32x' %(int(c_0,16) ^ int(pad_str,16) ^ int(atk_str,16))
		print "NEW C_0 =" +  new_c_0
		flag = po.query(iv+new_c_0+c_1)       # Issue HTTP query with the given argument
		if flag:
			saved_c_1 = y + saved_c_1
			print "SAVED_C_1 =" + saved_c_1
			break
	j = j-2
saved_c_0 = ""
j = 31
while j > 0:
	prefix = (j-1)/2
	suffix = (33 - j)/2
	#print j
	temp = iv[:j-1] + ("00"* suffix)
	print "Changed IV =" + temp
	for i in range(0,256):
		y = '%0.2x' %i
		pad_str = "00" * prefix + '%0.2x' %suffix * suffix
		atk_str = "00" * prefix + y + saved_c_0
		print "Pad_str IV =" + pad_str
		print "ATK_str IV =" +  atk_str
		#print int(pad_str,16)
		#print int(atk_str,16)
		new_iv = '%32x' %(int(iv,16) ^ int(pad_str,16) ^ int(atk_str,16))
		print "NEW IV =" + new_iv
		flag = po.query(new_iv+c_0)       # Issue HTTP query with the given argument
		if flag:
			saved_c_0 = y + saved_c_0
			print "SAVED_C_0 =" + saved_c_0
			break
	j = j-2

#print "Answer =" + saved_c_0 + saved_c_1 + saved_c_2
print "Answer =" + saved_c_0 + saved_c_1
