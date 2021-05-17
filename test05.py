from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("FuelConsumption.csv")
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
msk = np.random.rand(len(df))< 0.8
# print(msk)
train = cdf[msk]
test = cdf[~msk]
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_*train_x + regr.intercept_, '-r')

plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()