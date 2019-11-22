#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Final
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def insert(self, root, key):
        if root is None:
            root = TreeNode(key)
            return root
        else:
            if key > root.val:
                root.right = self.insert(root.right,key)
            else:
                root.left = self.insert(root.left,key)
            return root


            

    def search(self, root, key):
        if root is None :
            return False
        elif root.val == key:
            return True
        elif key > root.val:
            return self.search(root.right,key)
        elif key < root.val:
            return self.search(root.left,key)


        
    def inorder(self,root): 
        if root: 
            self.inorder(root.left) 
            print(root.val) 
            self.inorder(root.right) 
            
            
                    
    def findmin(self,root):
        while root.left is not None:
            root = root.left
        return root
    
    
    
    def delete(self,root,key):
        if root is None:
            return False
        elif key > root.val:
            root.right = self.delete(root.right, key)
        elif key < root.val:
            root.left = self.delete(root.left, key)


        else:   
            if root.left is None:
                replace = root.right  
                root = None            
                return replace         
            elif root.right is None:  
                replace = root.left
                root = None
                return replace

            
            else:  
                replace = self.findmin(root.right) 
                root.key = replace.key 
                root.right = self.delete(root.right,replace.key)
            return root


