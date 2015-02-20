'''
Created on 20 Feb 2015

@author: Kenneth O'Neill
'''
class NetworkNode():
    '''
    classdocs
    '''

    
    def add(self, ipaddress):
        self.hosts.append(ipaddress)

    
    def getAllHosts(self):
        return self.hosts
    
    def __init__(self):
        self.hosts = []
    