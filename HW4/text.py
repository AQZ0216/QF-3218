#%%
import requests
from bs4 import BeautifulSoup
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.family'] = ['Noto Sans CJK TC']

#%%
r = requests.get('http://www.qf.nthu.edu.tw/p/412-1366-4556.php')
soup = BeautifulSoup(r.text, 'html.parser')

p_tags = soup.find(id="editor").find_all('p')
text = ['']*4
text[0] = p_tags[1].get_text()
text[1] = p_tags[2].get_text()
text[2] = p_tags[3].get_text()
text[3] = p_tags[4].get_text()

#%%
dictionary = {'金融', '人才', '數理', '美國', '商品', '專業', '財務', '財經', '華爾街', '衍生性'}

result = list(text)

for txt, i in zip(result, range(4)):
    for word in dictionary:    
        idx = 0
        while(txt.find(word, idx) != -1):
            space = 0
            idx = txt.find(word, idx)
            if txt[idx-1] == ' ':
                temp = txt[0:idx+len(word)]
            else:
                temp = txt[0:idx] + ' ' + txt[idx:idx+len(word)]
                space += 1
            if txt[idx+len(word)] == ' ':
                txt = temp + txt[idx+len(word):]
            else:
                txt = temp + ' ' + txt[idx+len(word):]
                space += 1
            idx += len(word) + space
    result[i] = txt

#%%
f = open('text.txt', 'w')

for i in result:
    f.writelines(i + '\n')

f.close()

#%%
record = {}

for t in text:
    length = len(t)
    for i in range(length-1):
        key = t[i:i+2]
        value = record.get(key, 0)
        record[key] = value+1

record_sort = sorted(record.items(), key=lambda x:x[1], reverse=True)
rank = list(zip(*record_sort))

x = np.arange(10)
plt.bar(x, rank[1][0:10])
plt.xticks(x, rank[0][0:10])