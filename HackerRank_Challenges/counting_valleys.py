# solution of https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(n, s):
    count = 0
    flag = True
    def check(s,i):
        if s[i] == "U":
            return False
        return True
    altitude = 0
    for i in range(0,len(s)):
        if altitude == 0:
            flag = check(s, i)
        if s[i] == "U":
            altitude = altitude + 1
        else:
            altitude = altitude - 1
        if altitude == 0:
            if flag:
                count = count + 1
    return count 
