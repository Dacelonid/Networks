'''
Created on 24 Feb 2015

@author: eeikonl
'''
import unittest
from Networks.ManagedAddress import ManagedAddress


class ManagedAddressTest(unittest.TestCase):


    def test_ManagedAddressWithExactIpAddress(self):
        address1 = ManagedAddress("192.168.0.1")
        address2 = ManagedAddress("192.168.0.1")
        
        self.assertEqual(address1, address2)


    def test_ManagedAddressWithDifferentIpAddress(self):
        address1 = ManagedAddress("192.168.0.1")
        address2 = ManagedAddress("192.168.0.2")
        
        self.assertNotEquals(address1, address2)

    def test_ManagedAddressWithIpAddressAndSubnet(self):
        address1 = ManagedAddress("192.168.0.1")
        address2 = ManagedAddress("192.168.0/16")
        
        self.assertEquals(address1, address2)

    def test_ManagedAddressWithIpAddressAndDifferentSubnet(self):
        address1 = ManagedAddress("192.168.0.1")
        address2 = ManagedAddress("192.167.0/16")
        
        self.assertNotEquals(address1, address2)

    def test_ManagedAddressWithSubnetAndDifferentSubnet(self):
        address1 = ManagedAddress("192.168.0/16")
        address2 = ManagedAddress("192.167.0/16")
        
        self.assertNotEquals(address1, address2)

    def test_ManagedAddressWithSubnetAndDifferentIpAddress(self):
        address1 = ManagedAddress("192.168.0/16")
        address2 = ManagedAddress("192.167.0.1")
        
        self.assertNotEquals(address1, address2)

    def test_ManagedAddressWithSubnetAndIpAddress(self):
        address1 = ManagedAddress("192.168.0/16")
        address2 = ManagedAddress("192.168.0.1")
        
        self.assertEquals(address1, address2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()