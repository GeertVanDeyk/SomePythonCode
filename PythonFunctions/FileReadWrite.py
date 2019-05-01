# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 06:54:32 2019

@author: gvandeyk
"""
# FileReadWrite.py
# functions for checking if a file exists, read from a file
# write to a file
import os


def fileExists(filePath):
    return (os.path.exists(filePath))


def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()


def readFile(filePath):
    if not fileExists(filePath):
        print('The file ' + filePath + 'does not exist - cannot read it')
        return ''
    else:
        fileHandle = open(filePath, 'r')
        data = fileHandle.read()
        fileHandle.close()
        return data


def openFileForWriting(filePath):
    fileHandle = open(filePath, 'w')
    return fileHandle


def closeFile(fileHandle):
    fileHandle.close()


def openFileForReading(filePath):
    if not fileExists(filePath):
        print('The file ' + filePath + 'does not exist - cannot read it')
        return ''
    else:
        fileHandle = open(filePath, 'r')
        return fileHandle


def writeALine(fileHandle, lineToWrite):
    lineToWrite = lineToWrite + '\n'
    fileHandle.write(lineToWrite)


def readALine(fileHandle):
    theLine = fileHandle.readline()
    # this is a check for attempts to read past EOF
    # if this occurs, return False (not a string value)
    # this also allows the caller to detect EOF
    if not theLine:
        return False
    else:
        # strip off the newline character
        theLine = theLine.rstrip('\n')
        return theLine
