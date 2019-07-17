# Solution of https://leetcode.com/problems/corporate-flight-bookings/

# correct solution but Time limit exceed error

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dict1 = {}
        for m in range(1,n+1):
            dict1[m] = 0
        for i in bookings:
            for j in range(i[0], i[1]+1):
                dict1[j] =  dict1[j] + i[2]
        return list(dict1.values())

      
# Proper solution => cumulative sum 

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookAns = [0]*n
        for i in bookings:
            bookAns[i[0]-1] += i[2]
            if(i[1] < n):
                bookAns[i[1]] -= i[2]
        
        for i in range(0,len(bookAns)-1):
            bookAns[i+1] += bookAns[i]
            
        return(bookAns)
