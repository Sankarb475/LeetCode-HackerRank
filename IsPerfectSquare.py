#solution of https://leetcode.com/problems/valid-perfect-square/

from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = int(sqrt(num))
        if float(num) == val * val:
            return True
        return False
