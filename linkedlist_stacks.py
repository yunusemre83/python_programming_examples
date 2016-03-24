# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 23:43:21 2016

@author: yemre
"""

class ListNode(object):
    
    def __init__(self,data=None):
        self.nextnode = None
        self.data = data
        
class LinkedList(object):
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def insert_at_front(self,data):
        
        new_node = ListNode(data)

        if (self.size==0):
            self.head = self.tail = new_node
        else:    
            temp_node = self.head 
            self.head = new_node
            new_node.nextnode = temp_node
        
        self.size = self.size + 1

    def insert_at_back(self,data):
        
        new_node = ListNode(data)
        if (self.size==0):
            self.head = self.tail = new_node
        else:     
            temp_node = self.tail 
            temp_node.nextnode = self.tail = new_node
 
        self.size = self.size + 1

    def remove_from_front(self):
        data = []
        if (self.size==0):
            return None 
        elif (self.size==1):
            data = self.head.data 
            self.head = self.tail = None
        else:
            data = self.head.data
            temp_node = self.head
            self.head = temp_node.nextnode
            
        self.size=self.size - 1    
        return data
        
    def remove_from_back(self):
        data = []
        if (self.size==0):
            return None 
        elif (self.size==1):
            data = self.head.data 
            self.head = self.tail = None
        else:
            data = self.tail.data
            temp_node = self.head
            while (temp_node.nextnode!=self.tail):
                temp_node = temp_node.nextnode

            self.tail = temp_node
            
        self.size=self.size - 1    
        return data
        
    def get_size(self):
        return self.size
        
    def isempty(self):
        if (self.size==0):
            return True
        else:
            return False
            
    def print_data(self):
        next_node = self.head
        for i in range(self.size):
            print(next_node.data)
            next_node = next_node.nextnode
    
    def reverse(self):
        if (self.size==0 or self.size==1):
            pass
        else:
            prev_node = None
            cur_node = self.head
            next_node = self.head.nextnode  
            
            while (prev_node!=self.tail):
                cur_node.nextnode = prev_node
                prev_node = cur_node
                cur_node = next_node
                if (cur_node is not None):
                    next_node = cur_node.nextnode

            temp_node = self.tail
            self.tail = self.head
            self.head = temp_node

print('TEST LINKEDLIST')
llist = LinkedList()  

for i in range(7):          
    if (i%2==0):    
        llist.insert_at_front(i)
    else:
        llist.insert_at_back(i)
        
print('list after insertions')
llist.print_data()

llist.reverse()

print('list after reversed:')    
llist.print_data()
    
print('remove from front:{}'.format(llist.remove_from_front()))
print('remove from back:{}'.format(llist.remove_from_back()))

print('list after reversed:')    
llist.print_data()

print('remove from front:{}'.format(llist.remove_from_front()))
print('remove from back:{}'.format(llist.remove_from_back()))

class stack(LinkedList):
    
    def __init__(self,max_size=10):
        LinkedList.__init__(self)
        self.max_size = max_size
    
    def push (self,data):
        
        if (self.max_size > self.size):
            self.insert_at_front(data)
            return True
            
        return False
        
    def pull (self):
        data = None
        if (self.size > 0):
            data=self.remove_from_front()
            
        return data
    
    def peek (self):
        data=None
        if (self.size > 0):
            data = self.head.data
        return data
             
print('TEST STACK')        
sstack = stack(5)

# push data
for i in range(7):          
    sstack.push(i)

print('stack after push:')
sstack.print_data()

print('peek top {}'.format(sstack.peek()))

# pull data
print('stack while pulling:')
for j in range(sstack.get_size()):
    print(sstack.pull())

# size after pulling    
print('size after pulling {}'.format(sstack.get_size()))  


class queue(LinkedList):
    
    def __init__(self,max_size=10):
        LinkedList.__init__(self)
        self.max_size = max_size
        
    def enqueue(self,data):
        
        if (self.max_size > self.size):
            self.insert_at_front(data)
            return True
        else:
            return False
        
    def dequeue(self):
        data = None
        if (self.size > 0):
            data=self.remove_from_back()
            
        return data

print('TEST QUEUE')        
qqueue = queue(5)

# enqueue data
for i in range(7):          
    qqueue.enqueue(i)

print('queue after enqueue:')
qqueue.print_data()

# dequeue data
print('queue while dequeue:')
for j in range(qqueue.get_size()):
    print(qqueue.dequeue())

# size after pulling    
print('size after dequeue {}'.format(qqueue.get_size()))  
        
  