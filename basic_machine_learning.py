# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:02:11 2020

@author: PC
"""


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split

data = pd.read_csv("Variables1.csv")

print(data.describe())

model = DecisionTreeRegressor()

data_x = ["Savings"]

x = data[data_x]
y = data.GDP

#decisiontree model
model_fit = model.fit(x,y)

plt.scatter(x, y)
plt.show()

#linear model
model_predict = model.predict(x)
print(model_predict)

regr = linear_model.LinearRegression()
regr.fit(x,y)
regr_prediction = regr.predict(x)
print(regr_prediction)

#errors
error_tree = mean_absolute_error(y, model.predict(x))
error_linear = mean_absolute_error(y, regr.predict(x))
error_linear_squared = mean_squared_error(y, regr.predict(x))
print("tree error is:", error_tree)
print("linear error is:",error_linear)
print("linear squared error is", error_linear_squared)

#train and test split
#decision tree regressor split
train_X, val_X, train_y, val_y = train_test_split(x, y,test_size = 0.20,random_state = 40)
new_model = DecisionTreeRegressor()
new_fit = new_model.fit(train_X,train_y)
new_predict = new_model.predict(val_X)

#linear regression split
new_train_x, new_val_x, new_train_y, new_val_y = train_test_split(x, y,test_size = 0.20,random_state = 40)
new_model_regr = linear_model.LinearRegression()
new_model_regr_fit = new_model_regr.fit(new_train_x,new_train_y)
new_model_regr_predict = new_model_regr.predict(new_val_x)


print("split mean error is:",mean_absolute_error(val_y, new_predict))
print("lnr regr split error is:", mean_absolute_error(new_val_y, new_model_regr_predict))

split_tree_error = (mean_absolute_error(val_y, new_predict))
split_regression_error = (mean_absolute_error(new_val_y, new_model_regr_predict))

#is the mea of decision tree regressor higher than linear regression model?
print(split_tree_error > split_regression_error)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 0)
    model.fit(train_X, train_y)
    tahmin = model.predict(val_X)
    hata = mean_absolute_error(val_y, tahmin)
    return(hata)

for max_leaf_nodes in [5,10,15,1000]:
    hatayi_al = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("dal sayisi:", max_leaf_nodes, "hata:", hatayi_al) 
    
