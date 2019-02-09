# solution of https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

#very fast and memory efficient

class RepeatedNTimesSolution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        list1 = []
        for i in A:
            if i in list1:
                return i
            else:
                list1.append(i)
