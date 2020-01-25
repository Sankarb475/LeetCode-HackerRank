# solution of https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i] + ar[j])%k == 0:
                count = count + 1
    return count
