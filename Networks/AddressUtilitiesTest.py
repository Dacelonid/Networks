'''
Created on 23 Feb 2015

@author: Kenneth
'''
import unittest
from AddressUtilities import NetmaskUtils

class IpAddressManagerTest(unittest.TestCase):
    def test_getAddressRange_1(self):
        lower, upper = NetmaskUtils.getAddressRange("192/1")
        self.assertEqual("128.0.0.0", lower)
        self.assertEqual("255.255.255.255", upper)
    
    def test_getAddressRange_2(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/2")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("255.255.255.255", upper)
        
    def test_getAddressRange_3(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/3")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("223.255.255.255", upper)
        
    def test_getAddressRange_4(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/4")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("207.255.255.255", upper)
        
    def test_getAddressRange_5(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/5")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("199.255.255.255", upper)
        
    def test_getAddressRange_6(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/6")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("195.255.255.255", upper)
        
    def test_getAddressRange_7(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/7")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("193.255.255.255", upper)
        
    def test_getAddressRange_8(self):    
        lower, upper = NetmaskUtils.getAddressRange("192/8")
        self.assertEqual("192.0.0.0", lower)
        self.assertEqual("192.255.255.255", upper)
        
    def test_getAddressRange_9(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255/9")
        self.assertEqual("192.128.0.0", lower)
        self.assertEqual("192.255.255.255", upper)

    def test_getAddressRange_10(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.160/10")
        self.assertEqual("192.128.0.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_11(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.160/11")
        self.assertEqual("192.160.0.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_12(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191/12")
        self.assertEqual("192.176.0.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_13(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.184/13")
        self.assertEqual("192.184.0.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_14(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.188/14")
        self.assertEqual("192.188.0.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_15(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.188/15")
        self.assertEqual("192.188.0.0", lower)
        self.assertEqual("192.189.255.255", upper)
        
    def test_getAddressRange_16(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.188/16")
        self.assertEqual("192.188.0.0", lower)
        self.assertEqual("192.188.255.255", upper)
        
    def test_getAddressRange_17(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.0/17")
        self.assertEqual("192.191.0.0", lower)
        self.assertEqual("192.191.127.255", upper)
        
    def test_getAddressRange_18(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.192/18")
        self.assertEqual("192.191.192.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_19(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.224/19")
        self.assertEqual("192.191.224.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_20(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.240/20")
        self.assertEqual("192.191.240.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_21(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.248/21")
        self.assertEqual("192.191.248.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_22(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.252/22")
        self.assertEqual("192.191.252.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_23(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.253/23")
        self.assertEqual("192.191.252.0", lower)
        self.assertEqual("192.191.253.255", upper)
        
    def test_getAddressRange_24(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.255/24")
        self.assertEqual("192.191.255.0", lower)
        self.assertEqual("192.191.255.255", upper)
        
    def test_getAddressRange_25(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.191.255.127/25")
        self.assertEqual("192.191.255.0", lower)
        self.assertEqual("192.191.255.127", upper)
        
    def test_getAddressRange_26(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.63/26")
        self.assertEqual("192.255.255.0", lower)
        self.assertEqual("192.255.255.63", upper)
        
    def test_getAddressRange_27(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.31/27")
        self.assertEqual("192.255.255.0", lower)
        self.assertEqual("192.255.255.31", upper)
        
    def test_getAddressRange_28(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.15/28")
        self.assertEqual("192.255.255.0", lower)
        self.assertEqual("192.255.255.15", upper)
        
    def test_getAddressRange_29(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.7/29")
        self.assertEqual("192.255.255.0", lower)
        self.assertEqual("192.255.255.7", upper)
        
    def test_getAddressRange_30(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.3/30")
        self.assertEqual("192.255.255.0", lower)
        self.assertEqual("192.255.255.3", upper)
        
    def test_getAddressRange_31(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.2/31")
        self.assertEqual("192.255.255.2", lower)
        self.assertEqual("192.255.255.3", upper)
        
    def test_getAddressRange_32(self):    
        lower, upper = NetmaskUtils.getAddressRange("192.255.255.255/32")
        self.assertEqual("192.255.255.255", lower)
        self.assertEqual("192.255.255.255", upper)
        
        
        
    def test_numberOfHosts(self):
        for x in range(1, 33):
            self.assertEqual(2 ** (32 - x), NetmaskUtils.howManyHosts("192.168.0.0/" + str(x)))
           

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'IpAddressManagerTest.testName']
    unittest.main()