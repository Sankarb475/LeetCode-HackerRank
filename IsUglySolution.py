#solution of ::  https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 2 == 0:
            num = num/2
        while num % 3 == 0:
            num = num/3
        while num % 5 == 0:
            num = num/5
        if num == 1:
            return True
        return False
    
#Recursive solution

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        return (num%2==0 and self.isUgly(num/2)) or (num%3==0 and self.isUgly(num/3)) or (num%5==0 and self.isUgly(num/5))
