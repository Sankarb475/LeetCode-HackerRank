# solution of https://leetcode.com/problems/sort-array-by-parity/

#very fast and memory efficient

class SortArrayByParitySolution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        listEven = []
        listOdd = []
        for a in A:
            if (a%2 == 0):
                listEven.append(a)
            else:
                listOdd.append(a)
                
        return listEven + listOdd
