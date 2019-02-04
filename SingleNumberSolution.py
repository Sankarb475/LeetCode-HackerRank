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

    
    # another way to slove this
    
from collections import Counter

class SingleNumberSolution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = dict(Counter(nums))
        for keys, values in a.items():
            if(values==1):
                return keys
        
        
                
            
        
