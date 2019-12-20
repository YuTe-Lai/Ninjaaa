#!/usr/bin/env python
# coding: utf-8

# In[65]:


from collections import defaultdict
  

class Graph:

    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  

    def BFS(self, s):
        visited = [0] * (len(self.graph)) 
        que = [] 
        que.append(s) 
        visited[s] = 1 
        while que:
            s = que.pop(0)
            print(s, end=',')
            for i in self.graph[s]:
                if visited[i] == 0:
                    que.append(i)
                    visited[i] = 1
                    

    def DFS(self, s):
        stack = []
        a=[]
        a.append(s) #直接把根放進去
        while len(a) != len(self.graph):
            for i in self.graph[s]:
                if i not in stack and i not in a:
                    stack.append(i)
            s=stack.pop(-1)
            a.append(s)
        return a

            
        


# In[ ]:




