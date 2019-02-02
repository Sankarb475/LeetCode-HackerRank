#Problem statement can be found here :: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0): return False
        if (int(str(abs(x))[::-1]) == x):
            return True
        return False


#a different way to solve the same problem

class IsPalindromeSolution:
    def isPalindrome(self, x):
        if (x<0): return False
        if(int(''.join(list(str(x))[::-1])) == x):
            return True
        return False
    
        
