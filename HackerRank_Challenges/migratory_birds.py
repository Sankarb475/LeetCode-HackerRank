# solution of https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    dict1 = {}
    for i in arr:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i] + 1
    max_val = [keys for keys,values in dict1.items() if values == max(dict1.values())]
    return min(max_val)
