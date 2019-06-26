# solution of https://leetcode.com/problems/verifying-an-alien-dictionary/


class Solution:
    def isAlienSorted(self, words: 'List[str]', order: 'str') -> 'bool':
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            length = min(len(word1), len(word2))
            if word1[:length] == word2[:length] and len(word2) == length:
                return False
            elif word1[:length] == word2[:length] and len(word1) == length:
                return True
            for j in range(length):
                letter1 = word1[j]
                letter2 = word2[j]
                if order.index(letter1) < order.index(letter2):
                    break
                if order.index(letter1) > order.index(letter2):
                    return False
        return True


class Solution:
    def isAlienSorted(self, words: 'List[str]', order: 'str') -> 'bool':
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            length = min(len(word1), len(word2))
            if word1[:length] == word2[:length] and len(word2) == length:
                return False
            for j in range(length):
                letter1 = word1[j]
                letter2 = word2[j]
                if order.index(letter1) < order.index(letter2):
                    break
                if order.index(letter1) > order.index(letter2):
                    return False
        return True
        
        
        
        
