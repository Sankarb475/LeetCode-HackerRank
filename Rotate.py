#solution of https://leetcode.com/problems/rotate-array/ 


# Time limit exceed error
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            for m in range(len(nums)-1,0,-1):
                a = nums[m]
                nums[m] = nums[m-1]
                nums[m-1] = a
        
        
        
# This works well if you have non negative integers

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        if k >= len(nums):
            count = 0
            while k>len(nums):
                k = k - count*len(nums)
                count = count+1
        val1 = [str(i) for i in nums]
        val2 = ''.join(val1)
        part1 = [int(i) for i in list(val2[:-k])]
        print(part1)
        part2 = [int(i) for i in list(val2[-k:])]
        print(part2)
        for i in range(len(part2)):
            nums[i] = part2[i]
        for i in range(len(part1)):
            nums[len(part2)+i] = part1[i]
        
        
