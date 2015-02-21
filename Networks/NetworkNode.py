'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''
class NetworkNode():
    '''
    classdocs
    '''

    
    def add(self, ipaddress):
        if "/" not in ipaddress:
            self.hosts.append(ipaddress)
        else:
            self.networks.append(ipaddress)

    
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

    
    def getIpPrefix(self, subnet):
        cidr = str.split(subnet, "/")[1]
        
        return "192.168"
    
    
    def getHostsWithinSubnet(self, subnet):
        ipPrefix = self.getIpPrefix(subnet)
        return [s for s in self.hosts if ipPrefix in s]
    
    
    
    
    