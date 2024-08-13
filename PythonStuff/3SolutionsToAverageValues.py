# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:52:23 2019

@author: gvandeyk
but probably taken from the internet - this you should not mention though
"""

from functools import reduce


def mysum(x, y):
    return float(float(x) + float(y))


InputData = input('Give me a series of float values : ').split()
OutputData = []
# store first value
OutputData.append(float(InputData[0]))
currIndex = 1
for allData in InputData[1:len(InputData)-1]:
    CurrentValue = float(InputData[currIndex])
    PreviousValue = float(InputData[currIndex - 1])
    NextValue = float(InputData[currIndex + 1])
    SumPart = CurrentValue + PreviousValue + NextValue
    NewValue = (SumPart / 3)
    OutputData.append(NewValue)
    currIndex += 1

# store last value
if len(InputData) > 1:
    OutputData.append(float(InputData[len(InputData)-1]))

print(' '.join(str(OutputData)))

print('second solution')
OutputData = []
# store first value
OutputData.append(float(InputData[0]))
currIndex = 1
for allData in InputData[1:len(InputData)-1]:
    sumPart = 0
    for x in list(InputData[currIndex - 1:currIndex + 2]):
        sumPart += float(x)
    NewValue = (sumPart / 3)
    OutputData.append(float(NewValue))
    currIndex += 1

# store last value
if len(InputData) > 1:
    OutputData.append(float(InputData[len(InputData)-1]))

print(' '.join(str(OutputData)))

print('third solution')


OutputData = []
# store first value
OutputData.append(float(InputData[0]))
currIndex = 1
for allData in InputData[1:len(InputData)-1]:
    OutputData.append(reduce(mysum, list(InputData[currIndex - 1:currIndex + 2])) / 3)
    currIndex += 1

# store last value
if len(InputData) > 1:
    OutputData.append(float(InputData[len(InputData)-1]))

print(' '.join(str(OutputData)))

