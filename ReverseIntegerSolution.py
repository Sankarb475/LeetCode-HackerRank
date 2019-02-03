# solution of https://leetcode.com/problems/reverse-integer/

class ReverseIntegerSolution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = int(str(abs(x))[::-1])
        if x>0 and a<(pow(2,31)-1):
            return a
        if x<0 and -a>pow(-2,31):
            return -a
        return 0
    
