# -*- coding: utf-8 -*-
"""Social_network_logistic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WKXd7qzdFEnHFqxJkl7UwFgWEDqWC_bh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('/content/Social_Network_Ads.csv')
df

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

df.head()

x=df[['Gender', 'Age' ,'EstimatedSalary']].values
y=df['Purchased'].values
print(x)
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train)
print(x_test)

print(len(x))

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
y_pred=logreg.predict(x_test)
print(x_test)

y_pred

y_test

from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

import seaborn as sns
class_names=[0,1]
fig, ax = plt.subplots()
import seaborn as sns
class_names=[0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
print()
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu",fmt='g')
ax.xaxis.set_label_position("top")

ax.xaxis.set_label_position("top")

print('accuracy: ' ,metrics.accuracy_score(y_test, y_pred))
print('accuracy: ' ,metrics.accuracy_score(y_test, y_pred))
print('precision: ',metrics.precision_score(y_test ,y_pred))
print('recall: ',metrics.recall_score(y_test, y_pred))
print("f1.score", metrics.f1_score(y_test, y_pred))