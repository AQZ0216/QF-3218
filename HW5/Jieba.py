#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import jieba

r = requests.get('http://www.qf.nthu.edu.tw/p/412-1366-4556.php')
soup = BeautifulSoup(r.text, 'html.parser')

p_tags = soup.find(id="editor").find_all('p')
text = ['']*4
text[0] = p_tags[1].get_text()
text[1] = p_tags[2].get_text()
text[2] = p_tags[3].get_text()
text[3] = p_tags[4].get_text()


# In[2]:


jieba.set_dictionary('../dict.txt.big.txt')
jieba.suggest_freq('賓大華頓學院', True)

f = open('text.txt', 'w')

for i in range(4):
    seg_list = jieba.cut(text[i])
    temp = " ".join(seg_list)
    f.write(temp+'\n')

f.close()


# In[ ]:




