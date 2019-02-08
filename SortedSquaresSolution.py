# solution of https://leetcode.com/problems/squares-of-a-sorted-array/


class SortedSquaresSolution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        list1 = []
        for i in A:
            list1.append(i**2)
        return sorted(list1)
