# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:09:22 2019

@author: gvandeyk
"""


def clock1(NumberOfMinutes=(24 * 60)):
    myHour = 0
    myMinutes = 0
    myHour_List = []
    myMinutes_List = []
    myHour_List.append('{:02d}'.format(myHour))
    myMinutes_List.append('{:02d}'.format(myMinutes))
    for myTime in range(NumberOfMinutes):
        if myMinutes == 59:
            myHour += 1
            myMinutes = 0
        else:
            myMinutes += 1
        myHour_List.append('{:02d}'.format(myHour))
        myMinutes_List.append('{:02d}'.format(myMinutes))
    return zip(myHour_List, myMinutes_List)


def clock2(NumberOfMinutes=(24 * 60)):
    myHour = 0
    myMinutes = 0
    myHour_List = []
    myMinutes_List = []
    for myTime in range(NumberOfMinutes):
        myHour_List.append(myHour)
        myMinutes_List.append(myMinutes)
        if myMinutes == 59:
            myHour += 1
            myMinutes = 0
        else:
            myMinutes += 1
            FormattedTimes = zip(['{:02d}'.format(x) for x in myHour_List],
                                 ['{:02d}'.format(x) for x in myMinutes_List])
            return FormattedTimes


# print(*(clock1()))

def timeCalc(inHr, inMin):
    if (inMin == 59):
       inHr += 1
       inMin = 0
    else:
       inMin += 1    
    return (inHr,inMin)


def clock3(NumberOfMinutes=(24 * 60)):
    myHour = 0 
    myMinutes = 0
    myHour_List = []
    myMinutes_List = []
    for myMinutes in range(NumberOfMinutes):
        myHour, myMinutes = timeCalc(myHour, myMinutes)
        myHour_List.append(myHour)
        myMinutes_List.append(myMinutes)
    return zip(['{:02d}'.format(x) for x in myHour_List],
               ['{:02d}'.format(x) for x in myMinutes_List])   

    
print(*clock3())

