# solution of https://www.hackerrank.com/challenges/utopian-tree/problem


def utopianTree(n):
    i = 0
    height = 1
    while i < n:
        i = i + 1
        if i%2 != 0:
            height = height * 2
        else:
            height += 1
    return height
