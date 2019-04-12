# solution of https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

#very fast and memory efficient

class RepeatedNTimesSolution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        list1 = []
        for i in A:
            if i in list1:
                return i
            else:
                list1.append(i)

                
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A = sorted(A)
        for i in range(1,len(A)):
            if A[i] == A[i-1]:
                return A[i]                
