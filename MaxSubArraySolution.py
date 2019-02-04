# solution of https://leetcode.com/problems/maximum-subarray/

# O(n) solution 
class MaxSubArraySolution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


# another way O(n^2) solution 
class MaxSubArraySolution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) ==1):
            return nums[0]
        dic = {}
        list1 = []
        list2 = nums[:]
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)+1):
                list1 = nums[i:j]
                if sum(list1) not in list2:
                    list2.append(sum(list1))
                list1 = []
            list2 = list(set(list2))
            
            
        return max(list2)
            
        
