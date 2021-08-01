# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/?ref=leftbar-rightbar

# finding pairs which will sum it to a given target

arr = [1, -2, 1, 0, 5]
sum = 3

for i in range(len(arr)):
    if (sum - arr[i]) in arr[i+1:]:
        print(sum,arr[i],sum-arr[i])
    
        
    
