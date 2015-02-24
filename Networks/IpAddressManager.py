'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''

from AddressUtilities import NetmaskUtils
from Networks.ManagedAddress import ManagedAddress
import pickle
class IpAddressManager():
    
    def add(self, ipaddress, note):
        self.managedNodes.append(ManagedAddress(ipaddress, note))
    
    def getAllManagedNodes(self):
        return self.managedNodes
    
    def __init__(self, filename):
        self.managedNodes = []  
        self.filename = filename

    def persist(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.managedNodes, f, pickle.HIGHEST_PROTOCOL)
    
    def read(self):
        with open(self.filename, 'rb') as f:   # will close() when we leave this block
            self.managedNodes = pickle.load(f)
        
    def isManaged(self, ipAddress):
        return ManagedAddress(ipAddress) in self.managedNodes

    def getHostsWithinSubnet(self, subNet):
        hosts = []
        for managedAddr in self.managedNodes:
            if managedAddr == subNet:
                if managedAddr.ipAddr != subNet.ipAddr: #Excluse exactly matching aub net address, as that is not a host
                    hosts.append(managedAddr)
        return hosts