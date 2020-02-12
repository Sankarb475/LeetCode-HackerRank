# solution of https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    maxval = max(height)
    if maxval - k < 0:
        return 0
    return maxval - k
