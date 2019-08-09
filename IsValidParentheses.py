# solution of https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        lefty = '[{('
        righty = ']})'
        S = []
        for i in s:
            if i in lefty:
                S.append(i)
            elif i in righty:
                if (not S) or (righty.index(i) != lefty.index(S.pop())):
                    return False
        return not S
                
