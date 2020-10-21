#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fredapi import Fred
fred = Fred(api_key='8b2b633b66efe5675eb70d56727016e2')
GDP = fred.get_series('GDPC1')
GDP.to_csv("real_GDP.csv")
UNRATE = fred.get_series('UNRATE')
UNRATE.to_csv("UNRATE.csv")


# In[ ]:




