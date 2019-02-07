# solution of https://leetcode.com/problems/sum-of-even-numbers-after-queries

# O(2n) solution

class SumEvenAfterQueriesSolution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        outList = []
        sumOut = 0
        for j in A:
            if j % 2 == 0:
                sumOut = sumOut + j
        out = 0
        for i in queries:
            A[i[1]] = A[i[1]] + i[0]
            if (A[i[1]] - i[0]) % 2 != 0:
                if A[i[1]] % 2 == 0:
                    sumOut = sumOut + A[i[1]]
                else:
                    sumOut = sumOut
            else:
                if A[i[1]] % 2 == 0:
                    sumOut = sumOut + i[0]
                else:
                    sumOut = sumOut - (A[i[1]] - i[0])
                    
            outList.append(sumOut)
        return outList
            
                
            
# O(n^2) solution 

class SumEvenAfterQueriesSolution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        outList = []
        sumOut = 0
        for i in queries:
            A[i[1]] = A[i[1]] + i[0]
            for j in A:
                if j%2 ==0:
                    sumOut = sumOut + j
            outList.append(sumOut)
            sumOut = 0
        return outList
            
        
