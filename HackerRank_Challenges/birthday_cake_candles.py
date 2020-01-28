# solution of https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(ar):
    ar.sort()
    return ar.count(ar[-1])
