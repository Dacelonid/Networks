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
    def getAddressRange(network):
        if "/" not in network:
            raise NameError("Not a valid network specification:" + network + " does not contain an address in CIDR notation")
        netaddr,bits = network.split('/')
        netaddr = NetmaskUtils.expandNetworkAddrIfNeeded(netaddr)
        networkPart = struct.unpack('>L', socket.inet_aton(netaddr))[0]
        networkMask = 4294967295 << (32 - int(bits))
        networkLower = networkPart & networkMask
        return socket.inet_ntoa(struct.pack("!I", networkLower)), socket.inet_ntoa(struct.pack("!I", networkLower + NetmaskUtils.howManyHosts(network)-1))
    
    @staticmethod
    def printAllPossibleHostsForSubnetMask(subnet):
        netaddr = subnet.split('/')[0]
        networkPart = struct.unpack('>L', socket.inet_aton(netaddr))[0]
        for x in range(networkPart, networkPart + NetmaskUtils.howManyHosts(subnet)):
            print(socket.inet_ntoa(struct.pack("!I", x)))
        
    @staticmethod
    def howManyHosts(subnet):
        netaddr,bits = subnet.split('/')
        hosts = 2 ** (32 - int(bits)) 
        return hosts