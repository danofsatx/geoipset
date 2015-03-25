#!/usr/bin/python3
# -*- coding: utf-8 -*-

# TODO:  Define variables
#        Bring in IP address from input
#        Get set names from ipset
#        return output to main
from dnf.pycomp import raw_input
from subprocess import check_output, CalledProcessError, getoutput

def get_ipaddress():
    ipaddr = raw_input("Enter IP address: ")
    return ipaddr

def get_ipsets():
    testset = getoutput("ipset list -n")
    return testset

def check_sets(ipaddr, testset):
    for ipset in testset:
        check_output(["/sbin/ipset", "-q", "test", "%s", "%s"]) % (ipset, ipaddr)
        if CalledProcessError == 0:
                #print "The IP is in the set." % (ipaddr, ipset)
            print("%s is in set %s.")
        else:
            print("%s is not blocked.") % (ipaddr)
                

check_sets(get_ipaddress(),get_ipsets())

"""try:
    output = check_output("/sbin/ipset", "-q", "test", "%s", "%s") %(testset,ipaddr) 
except CalledProcessError as e:
    print(e.returncode)"""