# solution of https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# generic solution 
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count = count + 1
        return count
   
   
# conditional solution based on the range of input value   
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if (i<100 and i >=10) or (i>=1000 and i <10000):
                count = count + 1
        return count
