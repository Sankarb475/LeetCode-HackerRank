# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# This algorithm does an extra round of traversing just to know that the list is already sorted.


# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:07:17 2020

@author: sankar biswas
"""

def BubbleSort(a):
    for i in range(len(a)):
        flag = True
        m = 0
        while m<len(a)-1:
            n = m +1
            if a[m] > a[n]:
                temp = a[m]
                a[m] = a[n]
                a[n] = temp
                flag = False
            m = m + 1
        if flag:
            return a    
          
list1 = [1,4,7,2,9,13,10]
print(BubbleSort(list1))
    
