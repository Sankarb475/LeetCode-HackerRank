# a = [-2,2,-3,4,-7]
a = [-5,-3]

def test(a):
    max_ending_here = a[0] 
    max_so_far = a[0]
    max_val = max(a)
    for i in range(len(a)):
        max_ending_here += i
        
        # theres no point going with a negative sum if max_ending_here is negative, because next positive outcome will give you better result
        if max_ending_here < 0:
            max_ending_here = 0
        
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here
            
    # in case all the elements of the list are negative, then max_so_far will be the first element of the list, might give erroneous outcome     
    if max_val > max_so_far:
        return max_val
    return max_so_far

print(test(a))




# if we would like to store the start and end indices, follow this 

#a = [-2,2,-3,4,-3,10]
a = [-5,-3]


def test(a):
    max_ending_here = a[0] 
    max_so_far = a[0]
    max_val = max(a)
    index_start = start = end = 0
    for i in range(len(a)):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0
            index_start = i +1
        
        elif max_ending_here > max_so_far:
            start = index_start
            end = i
            max_so_far = max_ending_here
            
    if max_val > max_so_far:
        return (max_val,a.index(max_val))
        
    return (max_so_far, start, end)

print(test(a))
