import time
import urllib2
from AppKit import NSBeep

def can_access_google():
    try:
        urllib2.urlopen('http://www.google.com')
        return True
    except urllib2.URLError:
        return False

while(True):
    print "Testing access to www.google.com"
    result = can_access_google()
    if(result):
        print "Success!"
        NSBeep()
        break
    else:
        print "Failed, will try again in 2 minutes"
    time.sleep(120)
