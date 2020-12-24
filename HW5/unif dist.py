#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random

popu = np.arange(40)
samp = []

for i in range(20):
    length = len(popu)
    temp = random.randint(0, length-1)
    samp.append(popu[temp])
    popu = np.delete(popu, temp)

print(samp)


# In[ ]:




