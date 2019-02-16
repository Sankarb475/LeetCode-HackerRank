# solution of https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

#have to come up with a different solution because this one is very slow 

class CountPrimeSetBitsSolution:
    def countPrimeSetBits(self, L: 'int', R: 'int') -> 'int':
        outCount = 0
        count = 0
        n = True
        for i in range(L,R+1):
            j = i
            while j not in [0,1]:
                if j %2 ==1:
                    count = count + 1 
                j = j // 2
                if j == 1:
                    count = count + 1
            if count ==1:
                count = 0
                continue
            elif count in [2,3]:
                outCount = outCount + 1
            else:
                if self.is_palindrome(count):
                    outCount = outCount + 1
            count = 0
        
        return outCount 
    
    def is_palindrome(self,count):
        for m in range(2,count//2 +1):
            if count%m == 0:
                count = 0
                return False
        return True
    
    
# another solution not created by me
class CountPrimeSetBitsSolution:
    def countPrimeSetBits(self, L, R):
        return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))
            
        
                    
                
                
                
                
                
                
            
            
        
