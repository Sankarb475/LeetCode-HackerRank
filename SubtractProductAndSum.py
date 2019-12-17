#solution of https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = list(str(n))
        sum1 = 0
        multiply = 1
        for i in a:
            sum1 = sum1 + int(i)
            multiply = multiply * int(i)
            
        return (multiply - sum1)
        
        
        
