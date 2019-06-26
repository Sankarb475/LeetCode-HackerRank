# solution of https://leetcode.com/problems/find-common-characters/

# Performance wise not good, have to work on optimizing it

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        newList = []
        output = []
        for m in A:
            newList.append(sorted(list(m)))
        smallestWord = min(newList, key=len)
        index = 0
        for i in range(len(smallestWord)):
            for j in range(len(newList)):
                if smallestWord[i] in newList[j]:
                    index = index + 1
                    if index == len(newList):
                        index = 0
                        output.append(smallestWord[i])
                        for k in range(len(newList)):
                            if newList[k] != smallestWord:
                                newList[k].remove(smallestWord[i])
                else:
                    index = 0
                    break
        return output
    
    
# solution is based on finding count of each char for all the strings, and the minimum count would be the max number count
# of occurence in all th elements

# fast and small 

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        firstWord = set(list(A[0]))
        output = []
        for i in firstWord:
            char_count = []
            for j in A:
                char_count.append(j.count(i))
            output.extend([i] * min(char_count))
        return output
    
    
    
    
    
                
          
