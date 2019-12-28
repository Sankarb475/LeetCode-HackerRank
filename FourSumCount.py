# solution of https://leetcode.com/problems/4sum-ii/

# Using Hash table(dictionary in Python) 
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        dict1 = {}
        for i in A:
            for j in B:
                if (i+j) in dict1:
                    dict1[i+j] = dict1[i+j] + 1
                else:
                    dict1[i+j] = 1
        for k in C:
            for l in D:
                if 0-l-k in dict1:
                    count = count + dict1[0-l-k]
        return count



# brute force solution - Time limit exceeds error
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        for i in A:
            for j in B:
                for k in C:
                    for l in D:
                        if i + j + k + l == 0:
                            count = count + 1
                            
        return count
        
