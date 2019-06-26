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
