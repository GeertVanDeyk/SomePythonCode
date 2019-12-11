# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:11:45 2019

@author: gvandeyk
"""
import pyodbc

MyPath = input('path where is the database : ')
MyDatabase = input('database file : ')
MyFilePath = (MyPath + MyDatabase).replace('\\', '/')
print('Path checked = ',MyFilePath)
MyAccessDriver = '{Microsoft Access Driver (*.mdb, *.accdb)}'

conn = pyodbc.connect(r'Driver=' + MyAccessDriver + ';DBQ=' + MyFilePath + ';')
cursor = conn.cursor()
cursor.execute('select * from table name')

for row in cursor.fetchall():
    print (row)