
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
#c_1 = "4a61044426fb515dad3f21f18aa577c0"
c_1 = "4a61044426fb515dad3f21f18aa577c8"
c_2 = "bdf302936266926ff37dbf7035d5eeb4"

temp = iv+c_0+c_1+c_2
print len(c_2)

flag = po.query(temp)       # Issue HTTP query with the given argument
