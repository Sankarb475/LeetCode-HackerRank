# In selection sort in each iteration you find the minimum value in the list and put it in front of the list. Swap the minimum value
# with the value in front of the list


# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:10:06 2020

@author: sb512911
"""

def selection(a):
    list2 = []
    for i in range(len(a)):
        minVal = a[i]
        for j in range(i,len(a)):
            if a[j] <=  minVal:
                minVal = a[j]
        idx = a.index(minVal)
        a[idx] = a[i]
        a[i] = minVal        
    return a
            
list1 = [1,4,7,2,9,13,10]
print(selection(list1))
