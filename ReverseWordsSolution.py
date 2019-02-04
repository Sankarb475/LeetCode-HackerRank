# solution of https://leetcode.com/problems/reverse-words-in-a-string/

import re
class ReverseWordsSolution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s.strip()) == 0:
            return ""
        s = re.sub(' +', ' ',s)
        a = s.split(" ")
        return ' '.join(a[::-1]).strip()
