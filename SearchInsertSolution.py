# solution of https://leetcode.com/problems/search-insert-position/

# follows normal binary search 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        mid = 0 
        while low<=high:
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
                if low > high:
                    return low
                
                
            elif nums[mid] > target:
                high = mid - 1
                if low > high:
                    return low
                


===================================================================================

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
        
            
