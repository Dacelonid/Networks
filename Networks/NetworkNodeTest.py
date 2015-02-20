'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''
import unittest
from Networks.NetworkNode import NetworkNode



class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_addNode_shouldBeAdded(self):
        objUnderTest = NetworkNode() 
        objUnderTest.add("192.168.0.1")
        self.assertEqual(["192.168.0.1"], objUnderTest.getAllHosts())

    def test_addMultipleNodes_shouldAllBeAdded(self):
        objUnderTest = NetworkNode() 
        objUnderTest.add("192.168.0.1")
        objUnderTest.add("192.168.0.2")
        objUnderTest.add("192.168.0.3")
        self.assertListEqual(["192.168.0.1","192.168.0.2","192.168.0.3"], objUnderTest.getAllHosts())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()