# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:00:39 2019

@author: gvandeyk
"""
import ReadEmail
import createMappingRecord

messagepath = 'C:/Users/gvandeyk/OneDrive - DXC Production/Downloads/'
messagefile = messagepath + 'SomeEmail.txt'

MyEmail = ReadEmail.readEmailFile(messagefile)
MappingRequest = ReadEmail.getEmailBody(MyEmail)
MappingRecord = createMappingRecord.createMappingRecord(MappingRequest)
print(MappingRecord)