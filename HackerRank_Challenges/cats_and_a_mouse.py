# solution of https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    if abs(z-x) > abs(z-y):
        return "Cat B"
    elif abs(z-x) < abs(z-y):
        return "Cat A"
    elif abs(z-x) == abs(z-y):
        return "Mouse C"
