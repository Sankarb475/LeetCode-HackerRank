#solution of this : https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/submissions/

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        list1 = []
     
        #creating the two-d array
        for i in range(n):
            list1.append([0] * m)    
        count = 0
        
        #manipulation
        for j in indices:
            list1[j[0]] = [i+1 for i in list1[j[0]]]
            #list1[j[1]] = [m+1 for m in list1[j[1]]]
            for m in list1:
                m[j[1]] = m[j[1]] + 1
                
        #counting the odd integers
        for i in list1:
            for j in i:
                if (j%2 != 0):
                    count = count + 1
              
        return count
            
            
        
