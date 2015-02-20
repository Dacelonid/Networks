'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''
import unittest
import os
from Networks.NetworkNode import NetworkNode



class Test(unittest.TestCase):


    def setUp(self):
        self.filename = "persisted_data"
        self.objUnderTest = NetworkNode(self.filename) 

    def tearDown(self):
        # if os.path.isfile(self.filename): 
          #  os.remove(self.filename)
        pass 


    def test_addNode_shouldBeAdded(self):
        self.objUnderTest.add("192.168.0.1")
        self.assertEqual(["192.168.0.1"], self.objUnderTest.getAllHosts())

    def test_addMultipleNodes_shouldAllBeAdded(self):
        for x in range(1,4):
            self.objUnderTest.add("192.168.0.%d" % (x) )
        self.assertListEqual(["192.168.0.1","192.168.0.2","192.168.0.3"], self.objUnderTest.getAllHosts())

    def test_addSubNets_shouldBeAddedToNetworks(self):
        self.objUnderTest.add("192.168/16")
        self.assertEqual([], self.objUnderTest.getAllHosts())
        self.assertEqual(["192.168/16"], self.objUnderTest.getAllNetworks())
    

    def readFromFile(self):
        with open(self.filename, 'r') as file:
            return [line.rstrip('\n') for line in file]

    def test_persistToFile(self):
        self.objUnderTest.add("192.168.0.1")
        self.objUnderTest.add("192.168.0.2")
        self.objUnderTest.persist()
        
        fileContents = self.readFromFile()
        self.assertEqual(["192.168.0.1", "192.168.0.2"], fileContents)
             

    def test_readDataFromPersistedFile(self):
        self.objUnderTest.add("192.168.0.1")
        self.objUnderTest.add("192.168.0.2")
        self.objUnderTest.add("192.168/16")
        self.objUnderTest.persist()
        
        newNetwork = NetworkNode(self.filename) 
        newNetwork.read()
        self.assertListEqual(["192.168.0.1","192.168.0.2"], self.objUnderTest.getAllHosts())
        self.assertListEqual(["192.168/16"], self.objUnderTest.getAllNetworks())
             

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()