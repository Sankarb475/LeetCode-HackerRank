# solution of https://leetcode.com/problems/reverse-string-ii/

# beats 100% in both memory and time

class ReverseStrSolution:
    def reverseStr(self, s: 'str', k: 'int') -> 'str':
        out = ""
        a=""
        for i in range(0,len(s)+1,2*k):
            a = s[i:i+k][::-1]
            out = out + a
            if i+k >= len(s)-1:
                out = out +  s[i+k:]
            else:
                out = out +  s[i+k:i+2*k]
            a=""
        return out
