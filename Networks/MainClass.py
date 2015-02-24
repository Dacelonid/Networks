'''
Created on 24 Feb 2015

@author: eeikonl
'''
from Networks.IpAddressManager import IpAddressManager
from AddressUtilities import NetmaskUtils


class MyClass(object):
    '''
    classdocs
    '''


    def printMenuAndGetChoice(self):
        print ("Welcome to the IP Address Manager:")
        print ("Your choices are:")
        print ("1: Add an IP Address to be managed")
        print ("2: List all managed IP Addresses")
        print ("3: List all IP Address for a given subnet")
        print ("4: Persist currently managed addresses to file")
        print ("5: Restore a previous presisted file")
        print ("x: Exit the program")
        choice = input("Choose your option=>>")
        return choice

    def start(self):
        manager = IpAddressManager("PersistedFile")
        choice = self.printMenuAndGetChoice()
        
        while choice != "x":
            if choice == "1":
                ipAddress = input("which IP Address do you want to add=>>")
                name = input("please enter a note:")
                manager.add(ipAddress, name)
                
            elif choice == "2":
                print (',\n'.join(map(str, manager.getAllManagedNodes())))
            elif choice == "3":
                subnet = input("which subnet do you want to check=>>")
                lower, upper = NetmaskUtils.getAddressRange(subnet)
                print("Range: " + str(lower) + " - " + str(upper) + " for " + str(NetmaskUtils.howManyHosts(subnet)) + " hosts")
            elif choice == "4":
                manager.persist()
            elif choice == "5":
                manager.read()
                
            choice = self.printMenuAndGetChoice()

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'IpAddressManagerTest.testName']
    MyClass().start()
