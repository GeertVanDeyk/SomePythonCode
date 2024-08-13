# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import preprocessing
import numpy as np

MyArray = np.array([[3.0, 1.0, 4.0], [1.0, 2.0, 3.0], [4.0, 2.0, 2.0]])
MyScaler = preprocessing.StandardScaler().fit(MyArray)
print('\nMyArray : \n', MyArray)
print('\nMyScaler : ', MyScaler)
print('\nMean : ', MyScaler.mean_)
print('\nScale : ', MyScaler.scale_)
print('\nStandardizedArray : \n', MyScaler.transform(MyArray))
