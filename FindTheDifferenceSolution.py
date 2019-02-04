# solution of https://leetcode.com/problems/find-the-difference/

class findTheDifferenceSolution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = list(t)
        b = list(s)
        list1 = [i for i in a if not i in b or b.remove(i)]
        return ''.join(list1)
        
        
