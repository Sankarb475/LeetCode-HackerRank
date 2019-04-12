# solution of https://leetcode.com/problems/n-repeated-element-in-size-2n-array/ 

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        list1 = []
        for a in A:
            if a in list1:
                return a
            else:
                list1.append(a)
            
