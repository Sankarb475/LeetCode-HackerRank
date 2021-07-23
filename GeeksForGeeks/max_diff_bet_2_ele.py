# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/


Time Complexity : O(n^2) 
Auxiliary Space : O(1)
=======================================================
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
    

    
Time Complexity : O(n) 
Auxiliary Space : O(1)   
=============================================================================  
# here we keep track of the minimum element encountered so far, and we subtract every element from that element
# since the bigger element has to be on the righter end, this solution helps

# a = [2, 3, 10, 6, 4, 8, 1] 
#output = 8

# a = [7, 9, 5, 6, 3, 2]

a = [1, 2, 90, 10, 110]

max_diff = a[1] - a[0]
min_element = a[0]

for i in range(1,len(a)):
    temp = a[i] - min_element
    if temp > max_diff:
        max_diff = temp
        
    if min_element > a[i]:
        min_element = a[i]
        
print(max_diff)

