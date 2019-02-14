# solution of https://leetcode.com/problems/reverse-words-in-a-string-iii/

# speed and memory both beats 100% others in python3

class ReverseWordsSolution:
    def reverseWords(self, s: 'str') -> 'str':
        p = s.split(" ")
        for i in range(len(p)):
            p[i] = p[i][::-1]
        return ' '.join(p)
            
        
