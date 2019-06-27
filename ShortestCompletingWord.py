#solution of https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        listOfLetters = [i for i in licensePlate if i not in ['1','2','3','4','5','6','7','8','9','0',' ']]
        print(listOfLetters)
        words = sorted(words, key=len)
        print(words)
        for i in words:
            print(i)
            for j in range(len(listOfLetters)):
                print(listOfLetters[j])
                if listOfLetters[j].lower() in i.lower():
                    if (j-1) == len(listOfLetters):
                        return i
                    continue
                else:
                    break
                    
        
