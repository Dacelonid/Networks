'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''
import unittest
import os
from Networks.IpAddressManager import IpAddressManager
from Networks.ManagedAddress import ManagedAddress
import pickle

class IpAddressManagerTest(unittest.TestCase):
    def setUp(self):
        self.filename = "persisted_data"
        self.objUnderTest = IpAddressManager(self.filename) 

    def tearDown(self):
        if os.path.isfile(self.filename): 
            os.remove(self.filename)

    def test_addNode_shouldBeAdded(self):
        self.objUnderTest.add("192.168.0.1")
        self.assertEqual([ManagedAddress("192.168.0.1")], self.objUnderTest.getAllManagedNodes())

    def test_addMultipleNodes_shouldAllBeAdded(self):
        for x in range(1, 4):
            self.objUnderTest.add("192.168.0.%d" % (x))
        self.assertListEqual([ManagedAddress("192.168.0.1"), ManagedAddress("192.168.0.2"), ManagedAddress("192.168.0.3")], self.objUnderTest.getAllManagedNodes())

    def test_addSubNets_shouldBeAddedToNetworks(self):
        self.objUnderTest.add("192.168/16")
        self.assertEqual([ManagedAddress("192.168/16")], self.objUnderTest.getAllManagedNodes())
    

    def readFromFile(self):
        with open(self.filename, 'rb') as f:  # will close() when we leave this block
            return pickle.load(f)
 
    def test_persistToFile(self):
        self.objUnderTest.add("192.168.0.1")
        self.objUnderTest.add("192.168.0.2")
        self.objUnderTest.persist()
         
        fileContents = self.readFromFile()
        self.assertEqual([ManagedAddress("192.168.0.1"), ManagedAddress("192.168.0.2")], fileContents)
              
 
    def test_readDataFromPersistedFile(self):
        self.objUnderTest.add("192.168.0.1")
        self.objUnderTest.add("192.168.0.2")
        self.objUnderTest.add("192.168/16")
        self.objUnderTest.persist()
         
        newNetwork = IpAddressManager(self.filename) 
        newNetwork.read()
        self.assertListEqual([ManagedAddress("192.168.0.1"), ManagedAddress("192.168.0.2"), ManagedAddress("192.168/16")], self.objUnderTest.getAllManagedNodes())
             
    def test_findNodesWithinSubNet(self):
        self.objUnderTest.add("192.168.0.1")
        self.objUnderTest.add("192.168.0.2")
        self.objUnderTest.add("10.168.0.2")
        self.objUnderTest.add("192.168/16")
        self.assertListEqual([ManagedAddress("192.168.0.1"), ManagedAddress("192.168.0.2")], self.objUnderTest.getHostsWithinSubnet(ManagedAddress("192.168.0/16")))
        self.assertListEqual([ManagedAddress("192.168.0.1"), ManagedAddress("192.168.0.2"), ManagedAddress("10.168.0.2")], self.objUnderTest.getHostsWithinSubnet(ManagedAddress("0/0")))
        
    def test_isHostManaged_checkingExplicitlyAddedHost(self):
        self.objUnderTest.add("192.168.0.1")
        self.assertTrue(self.objUnderTest.isManaged("192.168.0.1"))

    def test_isNetworkManaged_checkingExplicitlyAddedNetwork(self):
        self.objUnderTest.add("192.168/16")
        self.assertTrue(self.objUnderTest.isManaged("192.168/16"))
    
    def test_isHostManaged_checkingExplicitlyAddedNetwork(self):
        self.objUnderTest.add("192.168/16")
        self.assertTrue(self.objUnderTest.isManaged("192.168.0.1"))
    
    def test_findAllNodesWithinSubNet2(self):
        self.assertEqual(2, len(self.objUnderTest.findAllNodesWithinSubNet("255.255.255.254/31")))
        self.assertEqual(4, len(self.objUnderTest.findAllNodesWithinSubNet("255.255.255.252/30")))
        self.assertEqual(16, len(self.objUnderTest.findAllNodesWithinSubNet("255.255.255.240/28")))
        self.assertEqual(128, len(self.objUnderTest.findAllNodesWithinSubNet("255.255.255.128/25")))
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'IpAddressManagerTest.testName']
    unittest.main()
