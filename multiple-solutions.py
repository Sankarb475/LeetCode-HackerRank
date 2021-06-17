Solution of - https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == 'type':
                if i[0] == ruleValue:
                    count = count + 1
            elif ruleKey == 'color':
                if i[1] == ruleValue:
                    count = count + 1
            elif ruleKey == 'name':
                if i[2] == ruleValue:
                    count = count + 1
        return count
                    
            
       
=============================================================================================================
solution of - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        notequal = True
        length = 0
        if len(word1) > len(word2):
            length = len(word2)
        elif len(word2) > len(word1):
            length = len(word1)
        else:
            length = len(word1)
            notequal = False
        output = '' 
        for i in range(length):
            output = output + word1[i] + word2[i]
            
        if notequal:
            if len(word1) > len(word2):
                output = output + word1[length:]
            else:
                output = output + word2[length:]
        return output
                
            
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        notequal = True
        smallword = ''
        bigword = ''
        if len(word1) > len(word2):
            smallword = word2
            bigword = word1
        elif len(word2) > len(word1):
            smallword = word1
            bigword = word2
        else:
            smallword = word1
            notequal = False
        output = '' 
        for i in range(len(smallword)):
            output = output + word1[i] + word2[i]
            
        if notequal:
            output = output + bigword[len(smallword):]

        return output
                
            
            
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        for i in range(len(word1)):
            try:
                output = output + word1[i] + word2[i]
            except:
                output = output + word1[i:]
                break
            
        output = output + word2[len(word1):]
        return output






       
=============================================================================================================
solution of - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ''
        i,j = 0,1
        substring = ''
        flag = False
        listOut = []
        while j<len(s):
            if s[i].islower():
                if s[j] == s[i].upper():
                    if substring != '':
                        substring = substring + s[j]
                    else:
                        substring = substring + s[i] + s[j]
                    print('substring1 ', substring)
                    flag = True
                else:
                    if flag:
                        listOut.append(substring)
                        substring = ''
                        flag = False
            elif s[i].isupper():
                if s[j] == s[i].lower():
                    if substring != '':
                        substring = substring + s[j]
                    else:
                        substring = substring + s[i] + s[j]
                    print('substring2 ', substring)
                else:
                    if flag:
                        listOut.append(substring)
                        substring = ''
                        flag = False
            i = i + 1
            j = j + 1
            
        print(listOut)     
        return     
        

https://leetcode.com/problems/two-sum/  
=============================================================================================================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            check = target - nums[i]
            if check in nums[i+1:]:
                return [i,nums[i+1:].index(check)+i+1]
         
