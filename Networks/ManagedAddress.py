from Networks.AddressUtilities import NetmaskUtils
class ManagedAddress:
    
    def __init__(self, ipAddr):
        self.ipAddr = ipAddr
        
    def __eq__(self, other):
        if "/"  in self.ipAddr:
            if "/" in other.ipAddr:
                return self.ipAddr == other.ipAddr
            else:
                return self.addressInNetwork(other.ipAddr, self.ipAddr)
        else:
            if "/" in other.ipAddr:
                return self.addressInNetwork(self.ipAddr, other.ipAddr)
            else:
                return self.ipAddr == other.ipAddr
      
    def __str__(self):
        return self.ipAddr      
            
    def addressInNetwork(self, host,subnet):
        network_addr, masked_ipAddr = NetmaskUtils.getMaskForNetworkAndHost(host, subnet)
        return masked_ipAddr == network_addr
            