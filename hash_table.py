# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 22:22:33 2016

@author: yemre
"""

class HashTable(object):
    
    def __init__(self,size):
        
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size
        
    def put(self,key,data):
       
       hash_val = self.gethashvalue(key,len(self.slots))
       
       if (self.slots[hash_val] is None):
           self.slots[hash_val]=key
           self.data[hash_val]=data
       else:
           if(self.slots[hash_val]==key):
               self.data[hash_val]=data
           else:
               nexthash = self.rehashvalue(key,len(self.slots))
               
               while ((self.slots[nexthash] is not None) and (self.slots[nexthash] != key)):
                   nexthash = self.rehashvalue(nexthash,len(self.slots))
                   
               if (self.slots[nexthash] == None):
                   self.slots[nexthash]=nexthash
                   self.data[nexthash]=data
               else:
                   self.data[nexthash]=data

       
    def get(self,key):
        hash_val = self.gethashvalue(key,len(self.slots))
       
        if (self.slots[hash_val] == key):
            return self.data[hash_val]
        else:
            start_slot = hash_val
            nexthash = self.rehashvalue(key,len(self.slots))


            while (self.slots[nexthash] != key and (nexthash != start_slot)):
               nexthash = self.rehashvalue(nexthash,len(self.slots))

            if (self.slots[hash_val] == key):
                return self.data[hash_val]
            else:
                return None
               

    def gethashvalue(self,key,size):
        return key%size
    
    def rehashvalue(self,oldkey,size):
        return (oldkey+1)%size
        
    def __setitem__(self,key,data):
        self.put(key,data)
       
    def __getitem__(self,key):
        return self.get(key)   
        
        
        
myhash_tbl = HashTable(5)   
myhash_tbl[1] = 'one'
myhash_tbl[2] = 'two'
myhash_tbl[3] = 'three'
myhash_tbl[6] = 'seven'

print(myhash_tbl[2])   

myhash_tbl[1] = 'ONE'
print(myhash_tbl[1])   


