import time
import gevent
from gevent import socket
from AppKit import NSBeep

def can_access_popular_websites():
    urls = ['www.google.com', 'www.wikipedia.org']
    ip_numbers = lookup_ip_numbers_for(urls)
    return was_able_to_lookup_any_of_the_urls(ip_numbers)

def was_able_to_lookup_any_of_the_urls(ip_numbers):
    for ip_number in ip_numbers:
        if ip_number != None:
            return True
    return False

def lookup_ip_numbers_for(urls):
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=2)
    ip_numbers = [job.value for job in jobs]
    return ip_numbers

while(True):
    print "Testing web access"
    result = can_access_popular_websites()
    if(result):
        print "Success!"
        NSBeep()
        break
    else:
        print "Failed, will try again in 30 seconds"
    time.sleep(30)
