# solution of https://leetcode.com/problems/search-a-2d-matrix/

#Binary search 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        matrixOne = [j for i in matrix for j in i]
        left = 0
        right = len(matrixOne) -1
        while left <= right:
            mid = (left + right)//2
            if matrixOne[mid] == target:
                return True
            if matrixOne[mid] > target:
                right = mid - 1
            else:
                left = mid +1
            
                
            
            
                
    
