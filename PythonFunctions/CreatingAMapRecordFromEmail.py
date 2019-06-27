# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:00:39 2019

@author: gvandeyk
"""
from ReadEmail import readEmailFile, getEmailBody
import createMappingRecord

messagepath = input() + '/'
messagefile = (messagepath + input()).replace('\\','/')

MyEmail = readEmailFile(messagefile)
MappingRequest = getEmailBody(MyEmail)
MappingRecord = createMappingRecord.createMappingRecord(MappingRequest)
print(MappingRecord)