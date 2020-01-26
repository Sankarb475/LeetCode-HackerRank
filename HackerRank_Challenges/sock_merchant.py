# solution of https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    listCount = []
    dict1 = {}
    for i in ar:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    for key, value in dict1.items():
        listCount.append(value//2)
    return sum(listCount)
    
