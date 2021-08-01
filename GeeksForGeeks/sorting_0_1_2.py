# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/?ref=leftbar-rightbar

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

j = 0

for i in range(len(arr)):
    if arr[i] == 0:
        arr[i], arr[j] = arr[j], arr[i]
        j = j + 1
        

for i in range(j, len(arr)):
    if arr[i] == 1:
        arr[i], arr[j] = arr[j], arr[i]
        j = j +1
        
        
print(arr)
        
        
        
        
    

