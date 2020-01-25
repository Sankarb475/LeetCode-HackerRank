# solution of https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    count = 0
    for i in range(a[-1], b[0]+1):
        flag = True
        for j in a:
            if i%j == 0:
                continue
            else:
                flag = False
                break
        if flag:
            for j in b:
                if j%i == 0:
                    continue
                else:
                    flag = False
                    break
        if flag:
            count = count+1
    return count
