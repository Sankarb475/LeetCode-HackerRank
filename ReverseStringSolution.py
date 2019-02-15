# solution of https://leetcode.com/problems/reverse-string/

#memory efficient

class ReverseStringSolution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0, len(s)-1
        while j>i:
            s[i] = s[i] + s[j]
            s[j] = s[i][0]
            s[i] = s[i][1]
            i = i+1
            j = j-1
        
        
