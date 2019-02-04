#solution of https://leetcode.com/problems/degree-of-an-array/

class FindShortestSubArraySolution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = {}
        list1 = []
        list2 = []
        for item in nums:
            b[item] = b.get(item, 0) + 1
        maxVal = max(b.values())
        for keys, values in b.items():
            if values == maxVal:
                list1.append(keys)
        for i in list1:
            indices = [j for j, x in enumerate(nums) if x == i]
            list2.append(indices[len(indices) -1]- indices[0])
        return min(list2)+1
        
