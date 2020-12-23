#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = 4
M = 3
res = {i: [i**j for j in range(0, M+1)] for i in range(1, N+1)}
print(res)

