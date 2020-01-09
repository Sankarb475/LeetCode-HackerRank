# Merge Sort explanation ==> 



# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 07:45:27 2020

@author: sb512911 (sankar biswas)
"""

def MergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]
        
        MergeSort(L)
        MergeSort(R)
        
        i=j=k=0
        
        while i< len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i = i + 1
            else:
                a[k] = R[j]
                j = j + 1
            k = k + 1
        
        while i < len(L):
            a[k] = L[i]
            i = i + 1
            k = k + 1
            
        while j < len(R):
            a[k] =  R[j]
            j = j + 1
            k = k + 1
        
    return a
    
    
list1 = [1,4,3,7,5,13,10,11,1,9]
print(MergeSort(list1))

