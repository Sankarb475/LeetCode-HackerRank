#Solution of https://leetcode.com/problems/factorial-trailing-zeroes

"""
The logic is :
you keep deviding the number with 5 and keep adding the output until the number is less than 5.
ie :
[1123/5] = 224
[224/5] = 44
[44/5] = 8
[8/5]=1. It is less than 5, so we stop here.

The answer is = 224 + 44 + 8 + 1 =277
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        while n>=5:
            sum = sum + n//5
            n = n//5
        return sum
        
