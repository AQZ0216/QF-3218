#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

df = pd.read_excel('HW6.xlsx')

df = df.drop(0)
df = df.drop('Unnamed: 5', axis=1)
df.columns = ["time", "2330", "2303", "2882", "Rm", "rf"]

nonNAN_rf = np.isfinite(df['rf'].to_numpy(dtype=float))
x = df.index[nonNAN_rf]
y = df['rf'][nonNAN_rf]
f = interp1d(x, y)
df['rf'] = f(df.index)

df['2330-rf'] = df['2330']-df['rf']
df['2303-rf'] = df['2303']-df['rf']
df['2882-rf'] = df['2882']-df['rf']
df['Rm-rf'] = df['Rm']-df['rf']

nonNAN_2330 = np.isfinite(df['2330-rf'].to_numpy(dtype=float))
nonNAN_2882 = np.isfinite(df['2882-rf'].to_numpy(dtype=float))


# In[2]:


#2330
reg1 = LinearRegression().fit(df['Rm-rf'][nonNAN_2330].to_numpy().reshape(-1, 1), df['2330-rf'][nonNAN_2330].to_numpy().reshape(-1, 1))
reg2 = LinearRegression(fit_intercept=False).fit(df['Rm-rf'][nonNAN_2330].to_numpy().reshape(-1, 1), df['2330-rf'][nonNAN_2330].to_numpy().reshape(-1, 1))

pred1 = reg1.predict(df['Rm-rf'][nonNAN_2330].to_numpy().reshape(-1, 1))
pred2 = reg2.predict(df['Rm-rf'][nonNAN_2330].to_numpy().reshape(-1, 1))

print("Ri-rf = ", '%.2f'%(reg1.intercept_) , " + ", '%.2f'%(reg1.coef_[0]), "*(Rm-rf)", sep='')
print("Ri-rf = ", '%.2f'%(reg2.coef_[0]), "*(Rm-rf)", sep='')

plt.scatter(df['Rm-rf'][nonNAN_2330], df['2330-rf'][nonNAN_2330])
plt.plot(df['Rm-rf'][nonNAN_2330], pred1, color='r', label=r'w/ $\alpha$')
plt.plot(df['Rm-rf'][nonNAN_2330], pred2, color='g', label=r'w/o $\alpha$')
plt.legend()
plt.title("2330")


# In[3]:


#2303
reg1 = LinearRegression().fit(df['Rm-rf'].to_numpy().reshape(-1, 1), df['2303-rf'].to_numpy().reshape(-1, 1))
reg2 = LinearRegression(fit_intercept=False).fit(df['Rm-rf'].to_numpy().reshape(-1, 1), df['2303-rf'].to_numpy().reshape(-1, 1))

pred1 = reg1.predict(df['Rm-rf'].to_numpy().reshape(-1, 1))
pred2 = reg2.predict(df['Rm-rf'].to_numpy().reshape(-1, 1))

print("Ri-rf = ", '%.2f'%(reg1.intercept_) , " + ", '%.2f'%(reg1.coef_[0]), "*(Rm-rf)", sep='')
print("Ri-rf = ", '%.2f'%(reg2.coef_[0]), "*(Rm-rf)", sep='')

plt.scatter(df['Rm-rf'], df['2303-rf'])
plt.plot(df['Rm-rf'], pred1, color='r', label=r'w/ $\alpha$')
plt.plot(df['Rm-rf'], pred2, color='g', label=r'w/o $\alpha$')
plt.legend()
plt.title("2303")


# In[4]:


#2882
reg1 = LinearRegression().fit(df['Rm-rf'][nonNAN_2882].to_numpy().reshape(-1, 1), df['2882-rf'][nonNAN_2882].to_numpy().reshape(-1, 1))
reg2 = LinearRegression(fit_intercept=False).fit(df['Rm-rf'][nonNAN_2882].to_numpy().reshape(-1, 1), df['2882-rf'][nonNAN_2882].to_numpy().reshape(-1, 1))

pred1 = reg1.predict(df['Rm-rf'][nonNAN_2882].to_numpy().reshape(-1, 1))
pred2 = reg2.predict(df['Rm-rf'][nonNAN_2882].to_numpy().reshape(-1, 1))

print("Ri-rf = ", '%.2f'%(reg1.intercept_) , " + ", '%.2f'%(reg1.coef_[0]), "*(Rm-rf)", sep='')
print("Ri-rf = ", '%.2f'%(reg2.coef_[0]), "*(Rm-rf)", sep='')

plt.scatter(df['Rm-rf'][nonNAN_2882], df['2882-rf'][nonNAN_2882])
plt.plot(df['Rm-rf'][nonNAN_2882], pred1, color='r', label=r'w/ $\alpha$')
plt.plot(df['Rm-rf'][nonNAN_2882], pred2, color='g', label=r'w/o $\alpha$')
plt.legend()
plt.title("2882")


# In[5]:


#2330 VS 2882
nonNAN = nonNAN_2330 & nonNAN_2882

reg1 = LinearRegression().fit(df['2882'][nonNAN].to_numpy().reshape(-1, 1), df['2330'][nonNAN].to_numpy().reshape(-1, 1))
reg2 = LinearRegression(fit_intercept=False).fit(df['2882'][nonNAN].to_numpy().reshape(-1, 1), df['2330'][nonNAN].to_numpy().reshape(-1, 1))

pred1 = reg1.predict(df['2882'][nonNAN].to_numpy().reshape(-1, 1))
pred2 = reg2.predict(df['2882'][nonNAN].to_numpy().reshape(-1, 1))

print("Y = ", '%.2f'%(reg1.intercept_) , " + ", '%.2f'%(reg1.coef_[0]), "*X", sep='')
print("Y = ", '%.2f'%(reg2.coef_[0]), "*X", sep='')

plt.scatter(df['2882'][nonNAN], df['2330'][nonNAN])
plt.plot(df['2882'][nonNAN], pred1, color='r', label=r'w/ $\alpha$')
plt.plot(df['2882'][nonNAN], pred2, color='g', label=r'w/o $\alpha$')
plt.legend()
plt.title("2330 VS 2882")

epsilon1 = sum(df['2330'][nonNAN].to_numpy().reshape(-1, 1)-pred1)
epsilon2 = sum(df['2330'][nonNAN].to_numpy().reshape(-1, 1)-pred2)
print('\u03A3(\u03B51) =', epsilon1)
print('\u03A3(\u03B52) =', epsilon2)


# In[ ]:




