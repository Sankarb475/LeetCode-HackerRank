# solution of https://leetcode.com/problems/plus-one/     ==> Easy

#fast but not memory efficient

class PlusOneSolution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        for a in range(len(digits)):
            digits[a] = str(digits[a])
        a = list(str(int(''.join(digits)) + 1))
        for i in range(len(a)):
            a[i] = int(a[i])
        return a
