# Solution of https://leetcode.com/problems/relative-sort-array/

# a bit slow but memory efficient 100%

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newList = []
        newList1 = []
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j] == i:
                    newList.append(arr1[j])
        for m in arr1:
            if m not in newList:
                newList1.append(m)
        #print(newList)
        newList1 = sorted(newList1)
        newList.extend(newList1)
        return newList
