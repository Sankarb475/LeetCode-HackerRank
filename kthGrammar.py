# solution of https://leetcode.com/problems/k-th-symbol-in-grammar/

# Using recursion => time limit exceed error
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def recur(start, n):
            if n == 0:
                return start
            else:
                temp = ""
                for i in start:
                    if i == "0":
                        temp = temp + "01"
                    elif i == "1":
                        temp = temp + "10"
                return recur(temp, n-1)
            
        val = recur("0", N-1)
        return val[K-1]
       
       
# O(n^2) solution 
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        start = "0"
        temp = ""
        for i in range(N-1):
            for i in start:
                if i == "0":
                    temp = temp + "01"
                elif i == "1":
                    temp = temp + "10"
            start = temp
            temp = ""
            
        print(start)
        return start[K-1]

 
 # Wrong solution 
 
 class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        comp1 = "0110"
        comp2 = "1001"
        count_of_elements = 2**(N-1)
        print(count_of_elements)
        temp = ""
        flag = True
        for i in range(1, count_of_elements//2 + 2, 4):
            if flag:
                temp = temp + comp1
                flag = False
            else:
                temp = temp + comp2
                flag = True
        
        return temp[K-1]
                
            
            
            
            
            
            
                
            
        
            
            
                    
        
            
                
        
        
 
 
            
        
            
            
                    
        
            
                
        
        
