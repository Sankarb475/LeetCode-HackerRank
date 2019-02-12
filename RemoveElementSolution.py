# solution of https://leetcode.com/problems/remove-element/

class RemoveElementSolution:
    def removeElement(self, nums, val):
        i=0
        while i < len(nums):
            if nums[i] == val: nums.remove(nums[i])
            else: i+=1
        return len(nums)
        

# output is accurate but did not get accepeted

class RemoveElementSolution:
    def removeElement(self, nums, val):
        for a in nums:
            if a == val and nums.count(a) > 1:
                for i in range(nums.count(a)):
                    nums.remove(a)
            elif a == val:
                nums.remove(val)
        return nums                
