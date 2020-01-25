# solution of https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    if (v1 - v2) == 0:
        return "NO"
    val = (x2 - x1)/(v1 - v2)
    print(val)
    if int(val) == val and val>0:
        return "YES"
    else:
        return "NO"
