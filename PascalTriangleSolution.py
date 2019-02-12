# solution of https://leetcode.com/problems/pascals-triangle/    ==> Easy

#very fast but not memory effcient

class PascalTriangleSolution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        listOut = []
        for i in range(numRows):
            listOut.append([1]*(i+1))
            
        if numRows ==1 or numRows ==2:
            return listOut
        
        for i in range(2,numRows):
            for j in range(1,i):
                listOut[i][j] = listOut[i-1][j-1] + listOut[i-1][j]
            
        return listOut
