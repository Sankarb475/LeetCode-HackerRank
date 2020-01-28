# solution of https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    arr.sort()
    minSum = sum(arr[:4])
    maxSum = sum(arr[1:])
