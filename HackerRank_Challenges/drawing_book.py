# solution of https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    flag = True
    countLeft = 0
    countRight = 0
    if n%2==0:
        total_pages = n - 2
        if p == 1 or p == n:
            return 0
    else:
        total_pages = n - 3
        flag = False
        if p == 1 or p in [n,n-1]:
            return 0
    if flag:
        for i in range(2,n,2):
            countLeft = countLeft + 1
            if p in [i,i+1]:
                break
        for i in range(n-1,1,-2):
            countRight = countRight + 1
            if p in [i,i-1]:
                break
        return min(countRight, countLeft)
    else:
        for i in range(2,n-1,2):
            countLeft = countLeft + 1
            if p in [i,i+1]:
                break
        for i in range(n-2,1,-2):
            countRight = countRight + 1
            if p in [i,i-1]:
                break
        return min(countRight, countLeft)
