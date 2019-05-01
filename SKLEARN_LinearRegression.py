# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:09:16 2018

@author: gvandeyk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[0:49, [0]]
Y = iris.data[0:49, [1]]
fig, ax = plt.subplots(1, 1)
ax.scatter(X, Y)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
plt.show()

lm = linear_model.LinearRegression()
lm.fit(X, Y)

print('Models Intercept value : ', lm.intercept_)
print('Models Coefficient Sepal Length : ', lm.coef_)

X = iris.data[0:49, [0]]
Y = iris.data[0:49, [1]]
fig, ax = plt.subplots(1, 1)
ax.scatter(X, Y)
ax.plot(X, lm.predict(X), color='red')
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
plt.show()