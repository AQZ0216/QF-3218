import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_excel('Y9999.xlsx')

df.columns = ["ticket", "time", "price"]

length = len(df)
df["t"] = np.arange(length)
df["Dummy"] = [0 if x > pd.Timestamp('2008-08-29') else 1 for x in df["time"]]
df["1-D"] = 1-df["Dummy"]
df["Dx"] = df["Dummy"]*df["t"]
df["(1-D)x"] = df["1-D"]*df["t"]

reg1 = LinearRegression().fit(df[["Dx", "(1-D)x"]], df["price"])
reg2 = LinearRegression().fit(df[["Dummy", "1-D", "Dx", "(1-D)x"]], df["price"])

pred1 = reg1.predict(df[["Dx", "(1-D)x"]])
pred2 = reg2.predict(df[["Dummy", "1-D", "Dx", "(1-D)x"]])

print("y = ", '%.2f'%(reg1.intercept_) , " + ", '%.2f'%(reg1.coef_[0]), "*D*x + ", '%.2f'%(reg1.coef_[1]), "*(1-D)*x", sep='')
print("y = D*(", '%.2f'%(reg2.intercept_+reg2.coef_[0]), " + ", '%.2f'%(reg2.coef_[2]), "*D*x) + ",
      "(1-D)*(", '%.2f'%(reg2.intercept_+reg2.coef_[1]), " + ", '%.2f'%(reg2.coef_[3]), "*D*x)", sep='')

plt.plot(df["time"], df["price"])
plt.plot(df["time"], pred1, label='model1')
plt.plot(df["time"], pred2, label='model2')
plt.legend()