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


# In[ ]:


jieba.set_dictionary('../dict.txt.big.txt')
seg_list = jieba.cut(text[0])
print(", ".join(seg_list))
seg_list = jieba.cut(text[1])
print(", ".join(seg_list))
seg_list = jieba.cut(text[2])
print(", ".join(seg_list))
seg_list = jieba.cut(text[3])
print(", ".join(seg_list))


# In[ ]:




