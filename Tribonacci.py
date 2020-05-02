# solution of => https://leetcode.com/problems/n-th-tribonacci-number/submissions/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a, b, c = 0, 1, 1
        while n-2>0:
            temp = a + b + c
            a = b
            b = c
            c = temp
            n = n - 1
        return temp
    
    
    
# Recursive solution 
class Solution:
    def tribonacci(self, n: int) -> int:
        def trib(n, meme = {0:0,1:1,2:1}):
            if n in meme:
                return meme[n]
            else:
                meme[n] = trib(n-1) + trib(n-2) + trib(n-3)     
                return meme[n]
        return trib(n)
        
  
# Dynamic Programming
#Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each
# of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memo = []
        memo.append(0)
        memo.append(1)
        memo.append(1) 
        
        for i in range(3, n+1):
            memo.append(memo[i-1] + memo[i-2] + memo[i-3])
            
        return memo[n]
            

        
        
   
            
        
