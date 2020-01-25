# solution of https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    maxCount = 0
    minCount = 0
    minVal = scores[0]
    maxVal = scores[0]
    for i in range(1,len(scores)):
        if scores[i] > maxVal:
            maxCount = maxCount + 1
            maxVal = scores[i]
        elif scores[i] < minVal:
            minCount = minCount + 1
            minVal = scores[i]
    return [maxCount, minCount]
    
    
 # map() in python ::
 -- you pass a "function" and a "list of values" you want to pass to that function
list(map(str, [1,2,4])) => This gives a list of string values ['1','2','4']
"str" is the function here and we are passing 1, 2 and 4 respectively to "str"
