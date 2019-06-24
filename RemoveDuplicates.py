#Solution of https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


#Time limit exceed error while submitting, but logically correct

class Solution:
    def removeDuplicates(self, S: str) -> str:
        index = 0
        list1 = list(S)
        return ''
        while True:
            if len(list1) == 1:
                return list1[0]
            elif list1[index] == list1[index + 1]:
                list1.pop(index)
                list1.pop(index)
                if len(list1) == 0:
                    return ''
                index = 0
            else:
                index = index + 1
                if len(list1) == index + 1:
                    return ''.join(list1)


