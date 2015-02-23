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
    


    def expandNetworkAddrIfNeeded(self, netaddr):
        '''192.168/16 is not the same as 192.168.0/16 so this method expands 
        all network address to be a full 4 bytes, ie 192.168/16 become 192.168.0.0/16'''
        subNetLength = len(netaddr.split('.'))
        for x in range(0, 4 - subNetLength):
            netaddr = netaddr + ".0"
        
        return netaddr

    def addressInNetwork(self, host,subnet):
        network_addr, masked_ipAddr = self.getMaskForNetworkAndHost(host, subnet)
        return masked_ipAddr == network_addr

    def getMaskForNetworkAndHost(self, host, subnet):
        networkMask, netaddr, ipaddr = self.getHostNetowrkAddrAndNetMask(host, subnet)
        networkPart = struct.unpack('>L',socket.inet_aton(netaddr))[0]
        ipaddr_masked = ipaddr & (networkMask)   # Logical AND of IP address and mask will equal the network address if it matches
        return networkPart, ipaddr_masked
    
    def getHostNetowrkAddrAndNetMask(self, host, subnet):
        ipaddr = struct.unpack('>L', socket.inet_aton(host))[0]
        netaddr, bits = subnet.split('/')
        netaddr = self.expandNetworkAddrIfNeeded(netaddr)
        networkMask = 4294967295 << (32 - int(bits))
        return networkMask, netaddr, ipaddr

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
        netaddr = subnet.split('/')[0]
        networkPart = struct.unpack('>L',socket.inet_aton(netaddr))[0]
        hosts = []
        for x in range(networkPart, 4294967295):
            hosts.append(socket.inet_ntoa(struct.pack("!I", x)) )
        return hosts