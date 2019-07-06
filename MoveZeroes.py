# solution of https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 # Shift count variable
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i-count], nums[i] = nums[i], nums[i-count] # Swap the nubmer and zero

        return

    
#esiest solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for elem in nums:
            if elem == 0:
                nums.remove(elem)
                nums.append(elem)    
