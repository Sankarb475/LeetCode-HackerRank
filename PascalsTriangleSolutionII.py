# solution of https://leetcode.com/problems/pascals-triangle-ii/      ==> easy

#fast but not memory effcient

class PascalsTriangleSolutionII:
    def getRow(self, numRows: 'int') -> 'List[int]':
        listOut = []
        numRows = numRows + 1
        for i in range(numRows):
            listOut.append([1]*(i+1))
            
        if numRows ==1:
            return [1] 
        if numRows ==2:
            return [1,1]
        
        for i in range(2,numRows):
            for j in range(1,i):
                listOut[i][j] = listOut[i-1][j-1] + listOut[i-1][j]
            
        return listOut[numRows - 1]
        
