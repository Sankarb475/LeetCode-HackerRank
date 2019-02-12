# solution of https://leetcode.com/problems/detect-capital/      ==> easy

#fast but not memory effcient

class DetectCapitalUseSolution:
    def detectCapitalUse(self, word: 'str') -> 'bool':
        m = True
        if len(word) ==1:
            return m
        for a in word:
            if ord(a)<=90 and ord(a)>=65:
                continue
            m = False
        if m:
            return True
        if not m:
            m = True
            for i in range(1,len(word)):
                if ord(word[i]) >= 97 and ord(word[i])<=122:
                    continue
                m = False
        return m
