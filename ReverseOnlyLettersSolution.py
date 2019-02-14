# solution of https://leetcode.com/problems/reverse-only-letters/

#very fast and memory efficient

class ReverseOnlyLettersSolution:
    def reverseOnlyLetters(self, S: 'str') -> 'str':
        dictionary = {}
        listStr = []
        for i in range(len(S)):
            if (ord(S[i])>=65 and ord(S[i])<=90) or (ord(S[i]) >=97 and ord(S[i])<=122):
                listStr.append(S[i])
            else:
                dictionary[i] = S[i]
        listStr = list(''.join(listStr)[::-1])
        for key,value in dictionary.items():
            listStr.insert(key,value)
        return ''.join(listStr)
        
        
        
        
                
                
        
