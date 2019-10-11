#!/usr/bin/env python
# coding: utf-8

# In[7]:


#ListNode

class ListNode:
    def __init__(self,data):
        self.data = data
        #store data
        
        self.next = None
        #store the reference(next item)
        return


# In[108]:


node1 = ListNode(15)
node2 = ListNode(666)


# In[92]:


#Single Linked-list
#由於每個節點只有指向下一個結點，而沒有指出上一個結點，所以屬於single linked-list，相對於有指出上一個節點的double linked-list。

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

#在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性。當我們加入一個新的節點時：
#若list本身還沒有任何節點，則head以及tail都會變成新的結點
#若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。


    def add_list_item(self,item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item  
        else:
            self.tail.next = item
        self.tail = item
        return
    
    def get(self, index)->int:
        if index<0 :
            return -1
        
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count
    
    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return
    
    
        
        


# In[113]:


list1 = SingleLinkedList()


# In[122]:


list1.add_list_item("fuck")


# In[124]:


list1.list_length()


# In[123]:


list1.output_list()


# In[ ]:


#https://stackabuse.com/python-linked-lists/
#https://leetcode.com/articles/design-linked-list/

