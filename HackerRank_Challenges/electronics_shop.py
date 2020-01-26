# solution of https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
    listOut = []
    for i in keyboards:
        for j in drives:
            sumT = i + j
            if sumT<=b:
                listOut.append(sumT)
    if not listOut:
        return -1
    return max(listOut)
