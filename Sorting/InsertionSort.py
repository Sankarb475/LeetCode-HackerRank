"""
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort 
removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no 
input elements remain.

In each iteration the sorted sublist is increasing form the begining

4  3  2  10

3  4  2  10

2  3  4  10

2  3  4  10
"""

# -*- coding: utf-8 -*-

def insertion(a):
    for i in range(1,len(a)):
        for j in range(i):
            if a[i] <= a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    return a

list1 = [14,46,43,27,57,41,45,21,70,0]
print(insertion(list1))

