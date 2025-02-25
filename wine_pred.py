# -*- coding: utf-8 -*-
"""wine pred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vm3mNjfynUeLZywKwl89keoL8b9UbYLu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns

wine_data = pd.read_csv('/content/winequality-red.csv')

wine_data.head(5)

wine_data.shape

wine_data.info()

"""chek if there is a missing value"""

wine_data.isnull().sum()

wine_data.describe()

wine_data.columns

"""now we wil do EDA"""

sns.catplot(x='quality',data=wine_data,kind='count')

plt.figure(figsize=(5,5))
sns.barplot(x='quality',y='citric acid',data=wine_data)

plt.figure(figsize=(5,5))
sns.barplot(x='quality',y='volatile acidity',data=wine_data)

correlation = wine_data.corr()
print(correlation)

"""plot a heatmap for more clarrification"""

plt.figure(figsize=(9,5))
sns.heatmap(correlation, cbar=True, cmap='Blues', annot_kws={'size':8}, annot=True, fmt = '.1f')

sns.pairplot(data=wine_data,hue='quality')

"""spliting the data adn label"""

X = wine_data.drop('quality',axis=1)
y = wine_data['quality']

print(X,y)

"""The given label data have contineos number so we create 2 classes 0 for bad wine and 2 for good wine"""

y = wine_data['quality'].apply(lambda y_value : 1 if y_value>=7 else 0 )

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print(X.shape,X_train.shape)

"""train our model"""

DT = DecisionTreeClassifier()

DT.fit(X_train,y_train)

predictions = DT.predict(X_test)

score = accuracy_score(predictions,y_test)
print(score)

"""making a predictive system"""

input_data = (7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0)
input_array = np.asarray(input_data)
input_array_new = input_array.reshape(1,-1)
pred = DT.predict(input_array_new)
if (pred[0]==1):
  print('it is good wine')
else:
  print('is i bad wine')

"""we will chek the accuracy by utilizing other model"""

model = RandomForestClassifier()
model.fit(X_train,y_train)

model_pred = model.predict(X_test)

accuracy_score(model_pred,y_test)

from sklearn.ensemble import GradientBoostingClassifier

GBC = GradientBoostingClassifier(random_state=0)
GBC.fit(X_train, y_train)

pred_gbc = GBC.predict(X_test)

accuracy_score(pred_gbc,y_test)

