# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:24:55 2019

@author: gvandeyk
"""
import urllib
from urllib.request import urlopen
myurl = input('enter a website : ')
response = urllib.request.urlopen(myurl)

# print the complete HTTP response header
print(response.info())

# Check the content type - as everything is label : value, this can be a dict 
content_type = response.info()['Content-Type']
if content_type.startswith('text/html'):
    print('OK! - this is text/html')
else:
    print('Expecting text/html; received ' + content_type)
 