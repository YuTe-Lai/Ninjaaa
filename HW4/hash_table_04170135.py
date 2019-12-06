#!/usr/bin/env python
# coding: utf-8

# In[61]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

        
    def add(self, key):
        h = MD5.new()
        h.update(key.encode("UTF-8"))
        arr = int(h.hexdigest() , 16)%self.capacity
        if self.data[arr] is None:
            self.data[arr] = ListNode(h)        
        else:
            n = ListNode(h)
            o = self.data[arr]
            while o.next is not None:
                o = o.next
            o.next = n
        
        
        
        
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("UTF-8"))
        arr = int(h.hexdigest() , 16)%self.capacity
        brr = int(h.hexdigest() , 16)
        n = self.data[arr]
        if self.data[arr]:
            cur = n
            while n.val != brr and n.next:
                n = n.next  
            cur.next = n.next
        else:
            return

        

        
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("UTF-8"))
        arr = int(h.hexdigest() , 16)% self.capacity
        brr = int(h.hexdigest() , 16)
        head = self.data[arr]
        if head is None:
            return False
        else:
            while head.val != brr:
                head = head.next
                if head is None: 
                    return False
            return True           


# In[ ]:




