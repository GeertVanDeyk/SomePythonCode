# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:29:05 2019

@author: gvandeyk
"""


def bubbleSort(lst):
    '''
    Implementation of bubble sort algorithm
    '''
    for border in range(len(lst)-1, 0, -1):
        for i in range(border):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def quickSort(lst):
    if lst:
        return quickSort([x for x in lst[1:] if x < lst[0]]) + \
               [lst[0]] + \
               quickSort([x for x in lst[1:] if x >= lst[0]])
    return []  # <-- this takes care of any None values occurring


if __name__ == '__main__':
    list_to_sort = [27, 0, 71, 70, 27, 63, 90]
    list_to_sort = list("My Black Dog")
    print(bubbleSort(lst=list_to_sort))
    print(quickSort(lst=list_to_sort))
