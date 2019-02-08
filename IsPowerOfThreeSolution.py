# solution of https://leetcode.com/problems/power-of-three/


from math import pow

class IsPowerOfThreeSolution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        m = True
        i = 0
        while m:
            a = pow(3,i)
            i = i+1
            if (a>n):
                return False
            elif a == n :
                return True
            else:
                continue
        
            
            
