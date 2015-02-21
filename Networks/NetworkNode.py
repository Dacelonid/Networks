'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''

import socket,struct

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

   
    def getHostsWithinSubnet(self, subnet):
        return [host for host in self.hosts if self.addressInNetwork(host, subnet)]
    
    def addressInNetwork(self, host,subnet):
        '''Method shamelessly stolen from Stackoverflow. Need to replace with my own method'''
        ipaddr = struct.unpack('>L',socket.inet_aton(host))[0]
        netaddr,bits = subnet.split('/')
        netmask = struct.unpack('>L',socket.inet_aton(netaddr))[0]
        ipaddr_masked = ipaddr & (4294967295<<(32-int(bits)))   # Logical AND of IP address and mask will equal the network address if it matches
        if netmask == netmask & (4294967295<<(32-int(bits))):   # Validate network address is valid for mask
            return ipaddr_masked == netmask
        else:
            print ("***WARNING*** Network",netaddr,"not valid with mask /"+bits)
            return ipaddr_masked == netmask
            

    
    
    