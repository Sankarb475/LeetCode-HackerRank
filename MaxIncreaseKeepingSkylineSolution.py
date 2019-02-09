# solution of https://leetcode.com/problems/max-increase-to-keep-city-skyline/    ==> (Medium level)

#very fast and memory efficient 

class MaxIncreaseKeepingSkylineSolution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        maxRow = []
        maxCol = []
        list1 = []
        sumOld = 0
        sumNew = 0
        for i in range(len(grid)):
            maxRow.append(max(grid[i]))
            for j in grid:
                list1.append(j[i])
            maxCol.append(max(list1))
            list1 = []
            sumOld = sumOld + sum(grid[i])
        for i in range(len(grid)):
            for j in range(len(grid)):
                grid[i][j] = min(maxRow[i],maxCol[j])
            sumNew = sumNew + sum(grid[i])
        return (sumNew - sumOld)
                          
            
