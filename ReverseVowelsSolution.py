# solution of https://leetcode.com/problems/reverse-vowels-of-a-string/


class ReverseVowelsSolution:
    def reverseVowels(self, s: 'str') -> 'str':
        listVowel = ['a','e','i','o','u']
        dictionary = {}
        count = 0
        for i in range(len(s)):
            if s[i].lower() in listVowel:
                dictionary[count] = i
                count = count + 1
        if len(dictionary) == 0:
            return s
        if len(dictionary) == len(s):
            return s[::-1]
        m, n = 0, len(dictionary)-1
        strList = list(s)
        
        while n>m:
            b = s[dictionary[m]]
            strList[dictionary[m]] = strList[dictionary[n]]
            strList[dictionary[n]] = b
            m = m+1
            n = n-1
        return ''.join(strList)
            
                
        
        
        
        
