# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:47:37 2019

@author: gvandeyk
"""

import string


def binarySearch(l, value):
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] > value:
            hi = mid - 1
        elif value > l[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    '''
    Note: binarySearch returns index (starting 0)
    '''
    test_list = [0, 1, 2, 3, 4, 5, 6]
    x = 6
    print(binarySearch(test_list, x))
    test_string = string.ascii_lowercase
    print(binarySearch(test_string, 'j'))
