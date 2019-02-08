# solution of https://leetcode.com/problems/fibonacci-number/

class FibonacciSolution:
    def fib(self, N: 'int') -> 'int':
        if N == 0:
            return 0
        if N==1:
            return 1
        element = 0
        i = 2
        a = 0
        b = 1
        while i<=N:
            element = a + b
            a = b
            b = element
            i = i+1
        return element
            
        
