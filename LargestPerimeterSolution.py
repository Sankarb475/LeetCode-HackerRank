#solution of https://leetcode.com/problems/largest-perimeter-triangle/

class LargestPerimeterSolution:
    def largestPerimeter(self, A):
        A = sorted(A)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
 

# Another solution, slow but accurate

import itertools

class LargestPerimeterSolution:
    def largestPerimeter(A: 'List[int]') -> 'int':
        b = list(itertools.combinations(A, 3))
        list1 = [0]
        for i in b:
            c = sorted(i)
            if c[0] + c[1] > c[2]:
                list1.append(sum(c))

        return max(list1)
