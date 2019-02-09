# solution of https://leetcode.com/problems/prime-palindrome/

# slow and not accepted but accurate

class Solution:
    def primePalindrome(self, N):
        m = True
        if (N==1 or N ==2):
            return 2
        while m:
            if int(str(N)[::-1]) == N:
                if self.is_prime(N):
                    return N
            N = N + 1
            
    def is_prime(self,b):    
        if (b<6):
            for i in range(2,b):
                if b%i == 0:
                    return False
            return True
        for i in range (2,b//2+1):
            if b%i == 0 :
                return False
        return True 





# slow and not accepted but accurate

class PrimePalindromeSolution:
    def primePalindrome(self, N):
        return 1
        m = True
        if (N==1 or N ==2):
            return 2
        while m:
            if self.is_palindrome(N):
                if self.is_prime(N):
                    m = False
                    return N
            N = N + 1
            
    def is_prime(self,b):
        if (b<6):
            for i in range(2,b):
                if b%i == 0:
                    return False
            return True
        for i in range (2,b//2):
            if b%i == 0 :
                return False
        return True 
        
    def is_palindrome(self, a):
        if int(str(a)[::-1]) == a:
            return True
        return False
