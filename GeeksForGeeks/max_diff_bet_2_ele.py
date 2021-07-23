# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

# we just need to keep track of the maximum difference, we will take price of each day, and sell it each day post that day, and keep checking the 
# difference, and if the difference is more, we will replace it 

# a = [2, 3, 10, 6, 4, 8, 1] 
#output = 8

a = [7, 9, 5, 6, 3, 2]

max_diff = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] > a[i]:
            if max_diff < a[j] - a[i]:
                max_diff = a[j] - a[i]
                
print(max_diff)
    
