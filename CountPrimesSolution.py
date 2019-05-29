#Algorithms used : Sieve of Eratosthenes
#Problem link : https://leetcode.com/problems/count-primes/


from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        count = -2
        is_prime = True
        if (n ==3):
            return 1
        if (n<=2):
            return 0
        list1 = [True] * n
        for i in range(2,int(sqrt(n))+1):
            if list1[i]:
                for j in range(i*i,n,i):
                    list1[j] = False
        #print(list1)
        for a in list1:
            if a:
                count = count + 1
        return count
        
