# solution of https://leetcode.com/problems/length-of-last-word/    ==> easy

# very very fast and not at all memory efficient :P

import re

class LengthOfLastWordSolution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        s = re.sub('[^A-Za-z0-9]+', ' ', s.strip())
        if len(s) == 1:
            return 1
        len(s.split(" ")[-1])
        return len(s.split(" ")[-1])
