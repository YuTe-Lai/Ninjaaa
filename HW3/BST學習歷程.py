#!/usr/bin/env python
# coding: utf-8

# In[6]:


class BST:
    def __init__(self):
        self.root = None
        
#一開始想說要先建一個BST ，但其實根本不用
#在使用的時候用Treenode(值)就好


# In[294]:


#搜尋
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def search(self,key):
        if 找不到的情況 :
            return None
        if 跟root一樣 :
            return key
        if 找到的情況跟root一樣 :
            return root
#先架構一下程式碼的樣子
    def search(self, key):
        if key < root:  
            跟leftchild比           #前兩個if 要弄成迴圈: return search(key)，
        if key > root:  #不過變數是key的話迴圈就沒意義，需要跟left/rightchild比較
            跟rightchild比         #所以重設fun() -> search(self,root,key)
        if key == root:
            return root
        else:
            return None


    
    def search(self, root, key):
        if key < root:
            return search(left, key)
        if key > root:
            return search(right, key)
        if key == root:
            return root
        else:
            return None
        # root應該是一個Node，應該會有left,right跟val，
        # 所以應該是要改成root.val
        
        
    def search(self,root, key):
        if key < root.val:
            return self.search(left, key) #search前要加self.才能取用
        if key > root.val:
            return self.search(right, key)
        if key == root.val:
            return root
        else:
            return None
#改成會回傳T/F
        
    def search(self, root, key):
        if root.val == key :
            return True
        elif root is None:
            return False
        else:
            if key > root.val:
                return self.search(root.right,key)
            else:
                return self.search(root.left,key)
#TRUE沒問題，False的時候會error
#把Flase換種方式寫
#AttributeError: 'NoneType' object has no attribute 'val'

    def search(self, root, key):
        if root.val == key :
            return True
        elif key > root.val:
            return self.search(root.right,key)
        elif key < root.val:
            return self.search(root.left,key)
        return False
#讓他跑完都沒有就回傳False
#AttributeError: 'NoneType' object has no attribute 'val'


    def search(self, root, key):
        if root is None :
            return False
        elif root.val == key:
            return True
        elif key > root.val:
            return self.search(root.right,key)
        elif key < root.val:
            return self.search(root.left,key)
#直接把False當第一句，沒問題


# In[ ]:





# In[166]:


#插入 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def insert(self,key):
        if root is None:
            root = TreeNode(key)          #迴圈出口
        if 比root大:
            跟rightchild比大小    #比完大小要插入 -> 迴圈
        if 比root小:                  #比大小需要跟root比
            跟leftchild比大小      #比完大小要插入 -> 迴圈
        else:
            跟root一樣(插左邊)    #迴圈出口
            
    def insert(self,root,key):
        if root.val is None:
            root = TreeNode(key)
        elif root.val < key:
            return insert(right,key)
        elif root.val > key:
            return insert(left,key)
        else:
            TreeNode(key).left = root.left   #一樣的話插左邊，
            root.left = TreeNode(key).root  #用要插入的node.val取代root.left
                                                        # 插入的node.left接上原本的root.left      
                                                        #這樣不知道妥不妥，決定給node加一個指向parent的指標
            

    def insert(self, root, key):
        if root == None:
            root = TreeNode(key)            
        elif root.val == key:
            TreeNode(key).parent = root.left
            root.parent = TreeNode(key).left
        else:
            if root.val < key:
                self.insert(root.right,key)
            else:
                self.insert(root.left,key)
#看起來沒問題，但fail



    def insert(self, root, key):
        if root is None:
            root = TreeNode(key)   
            return
        elif root.val == key:
            TreeNode(key).left = root.left    #有沒有parent這屬性都一樣
            root.left = TreeNode(key)
            return TreeNode(key)
            
        elif root.val < key:
            root.right = self.insert(root.right,key) #發現前面要加root.right/left = self.insert(..., ...)
        else:                                                 #這樣才會變，不然只是在耍智障
            root.left = self.insert(root.left,key)  

            
            
            
    def insert(self, root, key):
        if root is None:
            root = TreeNode(key)
            return root    #迴圈出口
        else:
            if key > root.val:
                root.right = self.insert(root.right,key)
            elif :
                root.left = self.insert(root.left,key)
            return root  #迴圈出口
#final整理一下


# In[ ]:





# In[302]:


#刪除
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class solution:
    def delete(self,root,key):
        if No Left或Right:
        elif Has One Left或Right:
        else Has Both Left或Right:
#先架構，分成三種情況刪除



    def delete(self,root,key):
        if root is None: #沒找到
            return False
        elif key > root.val:
            root.right = self.delete(root.right, key)
        elif key < root.val:
            root.left = self.delete(root.left, key)
#跟insert一樣，先找目標位子，無困難

        else:   #找到->root.val == key，開始刪
            if root.left is None:
                replace = root.right  #若左邊無子節，把右子節先存取起來
                root = None            #把root刪除
                return replace         #回傳右子節
            elif root.right is None:  #右邊同理
                replace = root.left
                root = None
                return replace
            #有一left/right情況
            
            else:  #有left/right,2子情況
                root.key = replace.key #取代
                #用右子集的min或左子集的max取代，所以再補一個def找取代值
                
                
                
                
    def findmin(self,root):
        if root.left is not None:
            root = self.findmax(root.left)
        else:
            return root
        #發現這樣弄出來會永遠None
        #改用while迴圈
        
    def findmin(self,root):
        while root.left is not None:
            root = root.left
        return root
    #找最小值，所以只要findmin(root.right)，就會跑出右子集最大值
    
    
    
    def delete(self,root,key):
        if root is None: #沒找到
            return False
        elif key > root.val:
            root.right = self.delete(root.right, key)
        elif key < root.val:
            root.left = self.delete(root.left, key)
#跟insert一樣，先找目標位子，無困難

        else:   #找到->root.val == key，開始刪
            if root.left is None:
                replace = root.right  #若左邊無子節，把右子節先存取起來
                root = None            #把root刪除
                return replace         #回傳右子節
            elif root.right is None:  #右邊同理
                replace = root.left
                root = None
                return replace
            #有一left/right情況
            
            else:  #有left/right,2子情況
                replace = findmin(root.right) #下面的取代是用這個取代
                root.key = replace.key #取代
                root.right = delete(root.right,replace.key)
            return root


# In[ ]:





# In[ ]:





# In[ ]:




