# solution of https://leetcode.com/problems/valid-palindrome/
import re

class IsPalindromeStringSolution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystring = s.lower()
        out1 = re.sub('[^A-Za-z0-9]+', '', mystring)
        if (out1[::-1] == out1):
            return True
        else:
            return False
            

        
