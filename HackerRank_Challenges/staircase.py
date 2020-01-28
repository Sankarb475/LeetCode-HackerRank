# solution of https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    output = " " * (n-1) + "#"
    for i in range(1, n):
        temp = " "*(n-i-1)+"#" * (i+1)
        output = output + '\n' + temp
    print(output)

