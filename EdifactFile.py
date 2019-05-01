import re


def createSegmentDictionary(DataContent):
    generatedDictionary = dict()
    for Lines in DataContent:
        elementsInLines = Lines.split()
        dict_key = (elementsInLines[0])
        dict_value = elementsInLines[1:]
        generatedDictionary[dict_key] = " ".join(map(str, dict_value))
    return generatedDictionary


def createContentDictionary(DataContent):
    generatedDictionary = dict()
    lineNumber = 0
    for Lines in DataContent:
        elementsInLines = (Lines.strip('\'\n')).split('+')
        lineNumber += 1
        dict_key = (lineNumber, elementsInLines[0])
        dict_value = elementsInLines[1:]
        generatedDictionary[dict_key] = dict_value
    return generatedDictionary


myRootPath = r'C:\Users\gvandeyk\OneDrive - DXC Production'
myPath = r'0 - ANALYSIS\000_Python\data'
myDataFile = r'EDIFACT_FILE.txt'
EdifactSegmentFile = r'EDIFACT SEGMENT TITLES.txt'

# read data
FileToOpen = myRootPath + '\\' + myPath + '\\' + myDataFile
f_Data = open(FileToOpen, 'r')
myFileContent = f_Data.readlines()
f_Data.close()

# read file of segment titles 
FileToOpen = myRootPath + '\\' + myPath + '\\' + EdifactSegmentFile
f_Segment = open(FileToOpen, 'r')
EdifactSegmentFileContent = f_Segment.readlines()
f_Segment.close()

theSegmentDictionary = createSegmentDictionary(EdifactSegmentFileContent)
myContentDictionary = createContentDictionary(myFileContent)

for k in myContentDictionary:
    if k[1] in theSegmentDictionary:
        print(k[1] + ' --- ' + theSegmentDictionary[k[1]])
        print(myContentDictionary[k])
        print()
