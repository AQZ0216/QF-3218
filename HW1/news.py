#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

r = requests.get('https://udn.com/news/story/12467/4915918')
soup = BeautifulSoup(r.text, 'html.parser')


# In[2]:


f = open('news.txt', 'w')
f.write(soup.h1.string+'\n\n\n\n')

p_tags = soup.article.find_all('p')
for tag in p_tags:
    f.write(tag.get_text())
f.close()


# In[ ]:




