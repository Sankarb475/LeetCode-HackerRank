# solution of https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    count = 0
    for i in range(0,len(s)):
        if sum(s[i:i+m]) == d:
            count = count + 1
    return count
