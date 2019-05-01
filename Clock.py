# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:46:30 2019

@author: gvandeyk
"""

class Clock():
    def __init__(self):
        self.clockHours = 0
        self.clockHoursLimit = 24
        self.clockMinutes = 0
        self.clockMinutesLimit = 60
        self.clockSeconds = 0
        self.clockSecondsLimit = 60

    def __addSeconds(self):
        self.clockSeconds += 1
        return self.clockSeconds 

    def runClock(self):
        self.__addSeconds()
        if self.clockSeconds == self.clockSecondsLimit:
            self.clockSeconds = 0
            self.clockMinutes += 1
        if self.clockMinutes == self.clockMinutesLimit:
            self.clockMinutes = 0
            self.clockHours += 1
        if self.clockHours == self.clockHoursLimit:
            self.clockHours = 0
        print('{:02d}'.format(self.clockHours) + ':' +
              '{:02d}'.format(self.clockMinutes) + ':' +
              '{:02d}'.format(self.clockSeconds))


if __name__ == "__main__":
    myClock = Clock()
    FullDay = 24 * 60 * 60
for x in range(FullDay):
    myClock.runClock()
