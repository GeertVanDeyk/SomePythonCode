# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:25:14 2018

@author: gvandeyk
"""

import numpy as np
import pandas as pd
import urllib

MyURL = 'http://aima.cs.berkeley.edu/data/iris.csv'
MyRequest = urllib.request.Request(MyURL)
TheResponse = urllib.request.urlopen(MyRequest)

MyDataFrame = pd.read_csv(TheResponse, sep=',', header=None, decimal='.',
                          names=['sepal_length', 'sepal_width',
                                 'petal_length', 'petal_width', 'target'])
print('\n', MyDataFrame.head(6))
print('\n', 'Total Number of rows : ', MyDataFrame['target'].count())
SetosaDataFrame = MyDataFrame[MyDataFrame['target'] == 'setosa']
print('\n', 'Total Number of rows in SetosaDataFrame  : ',
      MyDataFrame['target'].count())
print('\n', 'Mean petal length for Setosa : ',
      SetosaDataFrame['petal_length'].mean())
