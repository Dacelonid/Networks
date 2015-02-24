'''
Created on 23 Feb 2015

@author: eeikonl
'''
import socket,struct

class NetmaskUtils(object):
    '''
    classdocs
    '''
    @staticmethod
    def getHostNetowrkAddrAndNetMask(host, subnet):
        ipaddr = struct.unpack('>L', socket.inet_aton(host))[0]
        netaddr, bits = subnet.split('/')
        netaddr = NetmaskUtils.expandNetworkAddrIfNeeded(netaddr)
        networkMask = 4294967295 << (32 - int(bits))
        return networkMask, netaddr, ipaddr

    @staticmethod
    def expandNetworkAddrIfNeeded(netaddr):
        '''192.168/16 is not the same as 192.168.0/16 so this method expands 
        all network address to be a full 4 bytes, ie 192.168/16 become 192.168.0.0/16'''
        subNetLength = len(netaddr.split('.'))
        for x in range(0, 4 - subNetLength):
            netaddr = netaddr + ".0"
        
        return netaddr
    
    @staticmethod
    def getMaskForNetworkAndHost(host, subnet):
        networkMask, netaddr, ipaddr = NetmaskUtils.getHostNetowrkAddrAndNetMask(host, subnet)
        networkPart = struct.unpack('>L',socket.inet_aton(netaddr))[0]
        ipaddr_masked = ipaddr & (networkMask)   # Logical AND of IP address and mask will equal the network address if it matches
        return networkPart, ipaddr_masked
    
    @staticmethod
    def printAllPossibleHostsForSubnetMask(subnet):
        netaddr = subnet.split('/')[0]
        networkPart = struct.unpack('>L', socket.inet_aton(netaddr))[0]
        for x in range(networkPart, 4294967295 + 1):
            host = socket.inet_ntoa(struct.pack("!I", x))
            print(host)
        
    
    @staticmethod
    def howManyHosts(subnet):
        netaddr = subnet.split('/')[0]
        networkPart = struct.unpack('>L', socket.inet_aton(netaddr))[0]
        return 4294967295 + 1 - networkPart