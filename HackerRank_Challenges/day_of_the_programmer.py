# solution of https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def dayOfProgrammer(year):
    dict1 = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    sum = 0
    for key,value in dict1.items():
        sum = sum + value
        if sum>256:
            day = 256 - (sum - value)
            output = [day, key]
            break
    if year >= 1919:
        if year%400 == 0 or (year%4 == 0 and year%100!=0):
            return str(output[0]-1)+".0"+str(key)+"."+str(year)
        else:
            return str(output[0])+".0"+str(key)+"."+str(year)
    elif year <= 1917:
        if year%4 == 0:
            return str(output[0]-1)+".0"+str(key)+"."+str(year)
        else:
            return str(output[0])+".0"+str(key)+"."+str(year)
    elif year == 1918:
            return str(output[0]+13)+".0"+str(key)+"."+str(year)
