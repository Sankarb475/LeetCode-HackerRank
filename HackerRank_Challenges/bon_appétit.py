# solution of https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    sumT  = 0
    for i in range(len(bill)):
        if i!=k:
            sumT = sumT + bill[i]
    if sumT/2 == b:
        print("Bon Appetit")
    else:
        print(int((b*2 - sumT)/2))
