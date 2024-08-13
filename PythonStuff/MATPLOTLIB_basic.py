# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:36:25 2018

@author: gvandeyk
"""

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
x = np.arange(-10*pi, 10*pi, 0.01)
y = np.sin(x)/x
plt.style.use('ggplot')
line = plt.plot(x, y)
plt.setp(line, color='g', linewidth=2.0, linestyle='-')
plt.xlabel('x')
plt.ylabel('sinc(x)')
plt.show()
# showing customisation
pi = np.pi
x = np.arange(-10*pi, 10*pi, 0.01)
y = np.sin(x)/x
plt.style.use('ggplot')
line = plt.plot(x, y)
plt.setp(line, color='r', linewidth=3.0, linestyle='-.')
plt.xlabel('x')
plt.ylabel('sinc(x)')
