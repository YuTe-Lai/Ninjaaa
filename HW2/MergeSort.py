#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Merge Sort(合併排序法)：
#      概念：把陣列分解成子陣列直到只有一個元素，將子陣列解決後再將結果在合併。


# In[4]:


def merge_sort(arr):
    if len(arr)<=1:   #如果長度不大於1，就直接回傳
        print(arr)
    else:
        mid = len(arr)//2 # //->整數
        left = arr[:mid] 
        right = arr[mid:]
        merge_sort(left)      #分割完一次，左/右邊再進一次迴圈，直到每個陣列只剩1個元素
        merge_sort(right)
        return merge(l_arr,r_arr)


# In[2]:


a=[2,4,6,5,3,1,7]


# In[11]:


b=merge_sort(a)


# In[27]:


final = []
def merge_sort(arr):
    
    if len(arr)>1:                #改成如果長度的大於1，就開始分割
        mid = len(arr)//2     # //->整數
        left = arr[:mid] 
        right = arr[mid:]
        merge_sort(left)      #分割完一次，左/右邊再進一次迴圈，直到每個陣列只剩1個元素
        merge_sort(right)
        
        final_index = 0
        left_index = 0
        right_index = 0
    else:
        if left[left_index] < right[right_index]:
            final.append(left[left_index])
            left_index = left_index+1
            
        elif right[right_index] < left[left_index]:
            final.append(right[right_index])
            right_index = right_index+1
        else:
            final.append(left[left_index])
            left_index = left_index+1
            final.append(right[right_index])
            right_index = right_index+1
    return final

#UnboundLocalError: local variable 'left' referenced before assignment


# In[28]:


asd = [2,4,6,1,3,5,7]
zxc = merge_sort(asd)


# In[12]:


print(zxc)


# In[23]:


def merge(l_arr,r_arr):
    final = []
    l_index = 0
    r_index = 0
    final_index = 0
    if l_arr[l_index] < r_arr[r_index]:
            final.append(l_arr[l_index])
            l_index = l_index+1
        while r_arr[r_index] < l_arr[l_index]:
            final.append(r_arr[r_index])
            r_index = r_index+1
            
# Error : list index out of range 



# In[24]:





# In[5]:


def merge(l_arr,r_arr):
    final = []
    p = 0
    while l_arr[0] < r_arr[0]:
        final.append(l_arr[0])
        merge(l_arr[1:],r_arr)
    
    while r_arr[0] < l_arr[0]:
        final.append(r_arr[0])
        merge(l_arr,r_arr[1:])
#改用while迴圈


# In[ ]:


def merge_sort(arr):
    if len(arr)<=1:   
        print(arr)
    else:
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:]
        merge_sort(left)      
        merge_sort(right)
        return merge(l_arr,r_arr)

    
def merge(l_arr,r_arr):
    final = []
    p = 0
    while l_arr[0] < r_arr[0]:
        final.append(l_arr[0])
        merge(l_arr[1:],r_arr)
    
    while r_arr[0] < l_arr[0]:
        final.append(r_arr[0])
        merge(l_arr,r_arr[1:])
    
#NameError: name 'l_arr' is not defined


# In[9]:


def merge_sort(arr):
    if len(arr)<=1:   
        return arr
    else:
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:]
        l_arr = merge_sort(left)      
        r_arr = merge_sort(right)
    return merge(l_arr,r_arr)

    
def merge(l_arr,r_arr):
    final = []
    while l_arr[0] < r_arr[0]:
        final.append(l_arr[0])
        merge(l_arr[1:],r_arr)
        final = final + l_arr + r_arr
    
    while r_arr[0] < l_arr[0]:
        final.append(r_arr[0])
        merge(l_arr,r_arr[1:])
        final = final + l_arr + r_arr
    


# In[12]:


merge_sort(a)


# In[11]:


def merge_sort(arr):
    if len(arr)<=1:   
        return arr
    else:
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:]
        l_arr = merge_sort(left)      
        r_arr = merge_sort(right)
    return merge(l_arr,r_arr)

    
def merge(l_arr,r_arr):
    final = []
    while l_arr and r_arr:
        if l_arr[0] < r_arr[0]:
            
            final.append(l_arr[0])
            merge(l_arr[1:],r_arr)

        else:
            final.append(r_arr[0])
            merge(l_arr,r_arr[1:])    
            
        final = final + l_arr + r_arr
        return final


# In[13]:


a=[2,4,6,5,3,1,7]
merge_sort(a)


# In[4]:


# FINAL

def merge_sort(arr):
    if len(arr)<=1:   
        return arr
    else:
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:]
        l_arr = merge_sort(left)      
        r_arr = merge_sort(right)
        return merge(l_arr,r_arr)

    
def merge(l_arr,r_arr):
    final = []
    while l_arr and r_arr:
        if l_arr[0] < r_arr[0]:
            
            final.append(l_arr[0])
            del l_arr[0]

        else:
            final.append(r_arr[0])
            del r_arr[0]
            
    final = final + l_arr + r_arr
    return final


# In[5]:


a=[2,4,6,5,3,1,7]
merge_sort(a)


#參考資料：https://www.itread01.com/content/1550354967.html





