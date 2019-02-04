# solution of https://leetcode.com/problems/single-number/

class SingleNumberSolution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = list(set(nums))
        list1 = [i for i in nums if not i in b or b.remove(i)]
        return list(set(nums) - set(list1))[0]
