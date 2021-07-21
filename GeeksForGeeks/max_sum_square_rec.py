# Maximum of sum of length of rectangles and squares formed by given sticks
# https://www.geeksforgeeks.org/maximum-of-sum-of-length-of-rectangles-and-squares-formed-by-given-sticks/?ref=leftbar-rightbar


# My solution 
a = [1,1,2,2,3,3,3,3,11,11]
x = 15
# 22 and 30

dict_count = {}
square_sum = 0
rec_sum = 0

for i in range(len(a)):
    if a[i] not in dict_count:
        dict_count[a[i]] = 1
        
    else:
        dict_count[a[i]] +=1

square_side = 0    
rec_side_l = 0
rec_side_b = 0
print(dict_count)
for keys, values in dict_count.items():
    if values >=4:
        if keys > square_side:
            square_side = keys


for keys, values in dict_count.items():
    if values >=2 and keys!= square_side:
        if rec_side_l < keys:
            rec_side_b = rec_side_l
            rec_side_l = keys
            

print(square_side*4)
if rec_side_l != 0 and rec_side_b!=0:
    print(2*(rec_side_l+rec_side_b))
            





# GeeksForGeeks Solution
from collections import Counter
 
# Function to find the maximum of sum
# of lengths of rectangles and squares
# formed using given set of sticks
def findSumLength(arr, n) : 
     
    # Stores the count of frequencies
    # of all the array elements
    freq = dict(Counter(arr))
     
    # Stores frequencies which are at least 2
    freq_2 = {}
 
    for i in freq:
        if freq[i]>= 2:
            freq_2[i] = freq[i]
             
    # Convert all frequencies to nearest
    # smaller even values.
    arr1 = []
    for i in freq_2:
      arr1.extend([i]*(freq_2[i]//2)*2)
 
    # Sort the array in descending order
    arr1.sort(reverse = True)
 
    # Sum of elements up to
    # index of multiples of 4
    summ = 0
    for i in range((len(arr1)//4)*4):
        summ+= arr1[i]
         
    # Print the sum
    print(summ)
   
# Driver Code 
if __name__ == "__main__" : 
   
    arr = [1,1,2,2,3,3,3,3,11,11]; 
    n = len(arr); 
    findSumLength(arr, n);
