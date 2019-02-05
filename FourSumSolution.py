# solution of https://leetcode.com/problems/4sum/


import itertools

class FourSumSolution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        a = list(set(itertools.combinations(nums,4)))
        list1 = []
        for i in a:
            if sum(i) == target:
                list1.append(i)
        for a in range(len(list1)):
            p = list(list1[a])
            
        level1 = [list(row) for row in list1]
        for i in range(len(level1)):
            level1[i] = sorted(level1[i])
        list1 = []
        for a in level1:
            if a not in list1:
                list1.append(a)
        return list1
        
#proven to be a bit slow :P
