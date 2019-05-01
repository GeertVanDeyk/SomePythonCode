# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:55:06 2018

@author: gvandeyk
"""
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']
                    })
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']
                    })
df3 = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']
                    })
print('\n', pd.merge(df1, df2, on='key'))
print('\n', pd.merge(df1, df3, how='left', on='key'))
dfleft = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K1'],
                       'key2': ['K0', 'K1', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']
                       })
dfright = pd.DataFrame({'key1': ['K0', 'K0', 'K2', 'K1'],
                        'key2': ['K0', 'K1', 'K1', 'K2'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']
                        })
print('\n', pd.merge(dfleft, dfright, on=['key1', 'key2']))
