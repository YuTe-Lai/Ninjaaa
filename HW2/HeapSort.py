#!/usr/bin/env python
# coding: utf-8

# In[2]:


def heapify(arr, n, i): 
    large = i
    l = 2 * i + 1
    r = 2 * i + 2
    while arr[l]
        if len(arr)<=1:
            return arr
        else:
            if arr[i] < arr[l]:
                large = l
            if arr[large] < arr[r]:
                large = r
            if large != i:
                arr[i],arr[large] = arr[large],arr[i]
                heapify(arr, n, large)

#IndexError: list index out of range
            
def heapSort(arr):
    n = len(arr) 

    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 

arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 


# In[27]:


def swap(i, largest):                    
    arr[i], arr[largest] = arr[largest], arr[i] 


def heapify(n, i): 
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        swap(i, largest)
        heapify(n, largest) 

def heapSort(arr):
    n = len(arr) 

    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 

#IndexError: list index out of range


# In[32]:


def swap(i, o):                    
    arr[i], arr[o] = arr[o], arr[i] 


def heapify(n, i): 
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        swap(i, largest)
        heapify(n, largest) 

def heapSort(arr):
    n = len(arr) 

    for i in range(n, -1, -1): 
        heapify(n, i) 

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 


# In[36]:


# FINAL

def swap(g, h):                    
    arr[g], arr[h] = arr[g], arr[h] 

def heapify(n,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < n and arr[i] < arr[l]:   
        max = l   
    if r < n and arr[max] < arr[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(n, max)   

def heap_sort():     
    n = len(arr)   
    s = n // 2 - 1 
    for i in range(s, -1, -1):   
        heapify(n, i)   
    for i in range(n-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0) 


# In[ ]:


參考資料：
https://www.geeksforgeeks.org/python-program-for-heap-sort/
https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort

