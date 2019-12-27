#solution of https://leetcode.com/problems/valid-perfect-square/ ==> Binary search

# Using binary seacrh 
from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        end = num//2 + 1
        start = 1
        while end >= start:
            mid = (end + start)//2
            if mid * mid == num:
                return True
            elif mid*mid > num:
                end = mid - 1
            else:
                start = mid + 1
        return False


#using function
from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = int(sqrt(num))
        if float(num) == val * val:
            return True
        return False
