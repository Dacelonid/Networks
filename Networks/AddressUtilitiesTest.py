'''
Created on 23 Feb 2015

@author: Kenneth
'''
import unittest
from AddressUtilities import NetmaskUtils

class IpAddressManagerTest(unittest.TestCase):
    def test_getHostNetowrkAddrAndNetMask(self):
        networkMask, netaddr, ipaddr = NetmaskUtils.getHostNetowrkAddrAndNetMask("192.168.0.1", "255.255/16")
        print(networkMask, 2**16-1 << 16, 4294967295 << 16, 2**32 -1)
        print(netaddr)
        print(ipaddr)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'IpAddressManagerTest.testName']
    unittest.main()