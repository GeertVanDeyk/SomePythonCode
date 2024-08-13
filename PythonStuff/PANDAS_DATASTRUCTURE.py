# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:46:59 2018

@author: gvandeyk
"""
import numpy as np
import pandas as pd

MyDictionary = {'c_A': [1, 2, 3, 4],
                'c_B': [2, 4, 6, 8],
                'c_C': [3, 6, 9, 12],
                'c_D': [4, 8, 12, 16]
                }
MyDataFrame = pd.DataFrame(MyDictionary,
                           index=['r_One', 'r_Two', 'r_Three', 'r_Four'])

print(MyDataFrame)

MyDataFrame['c_NEW'] = MyDataFrame['c_C'] % 2 == 0
