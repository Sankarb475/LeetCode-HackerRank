# solution of https://leetcode.com/problems/search-insert-position/

class SearchInsertSolution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if(i == (len(nums)-1)):
                if(nums[i]<target):
                    return len(nums)
                else:
                    return i
            if(nums[i] > target):
                return i
        
            
