""" Ilk makine ogrenmesi modelim kutlu olsun. tarih 19.05.2020, 19 mayis Ataturk'un Samsun'a cikisi, genclik ve spor bayrami kutlu olsun, ne mutlu Turk'um diyene"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("/Users/PC/Desktop/data1.csv")
df.describe()
y = df.IQ
y.plot()
data_x = ["Age", "Major", "Exam Grade", "Paper Grade"]
X = df[data_x]
X.plot()
df_model = DecisionTreeRegressor(random_state = 1)
df_model.fit(X, y)
#print(X.head())
#print("the IQ predictions are listed below: ")
#print(df_model.predict(X))

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
df_model = DecisionTreeRegressor()
df_model.fit(train_X, train_y)
new_prediction = df_model.predict(val_X)
print(mean_absolute_error(val_y, new_prediction))




