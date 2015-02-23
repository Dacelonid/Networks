'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''

from AddressUtilities import AddressUtils

class NetworkNode():
    '''
    classdocs
    '''
    
    def add(self, ipaddress):
        if "/"  in ipaddress:
            self.networks.append(ipaddress)
        else:
            self.hosts.append(ipaddress)
    
    def getAllHosts(self):
        return self.hosts
    
    def getAllNetworks(self):
        return self.networks
    
    def __init__(self, filename):
        self.hosts = []
        self.networks = []
        self.filename = filename

    def persist(self):
        with open(self.filename, 'w') as file:
            for line in self.hosts:
                file.write(line +'\n')
        file.closed
    
    def read(self):
        with open(self.filename, 'r') as file:
            for line in file:
                self.add(line)
        file.closed

   
    def getHostsWithinSubnet(self, subnet):
        return [host for host in self.hosts if self.addressInNetwork(host, subnet)]
    
    def addressInNetwork(self, host,subnet):
        network_addr, masked_ipAddr = AddressUtils.getMaskForNetworkAndHost(host, subnet)
        return masked_ipAddr == network_addr

    def addressInAnyNetwork(self, host):
        for network in self.networks:
            if self.addressInNetwork(host, network):
                return True
        return False

    def isManaged(self, ipAddress):
        result = False
        if "/" in ipAddress:
            result =  ipAddress in self.networks
        else:
            result =  ipAddress in self.hosts or self.addressInAnyNetwork(ipAddress)
        return result
    

    def findAllNodesWithinSubNet(self, subnet):
        return AddressUtils.getAllHostsWithinSubnet(subnet)