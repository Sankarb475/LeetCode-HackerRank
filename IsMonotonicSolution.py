# solution of https://leetcode.com/problems/monotonic-array/

# very fast and memory effcient

class IsMonotonicSolution:
    def isMonotonic(self, A: 'List[int]') -> 'bool':
        if len(A) < 3:
            return True
        if A[0] <= A[-1] and A[1] <= A[-1]:
            m = 1
        elif A[0] >= A[-1] and A[1] >= A[-1]:
            m = 0
        else:
            return False
        if m ==1:
            for i in range(0,len(A) -1):
                if (A[i] <= A[i+1]):
                    continue
                else:
                    return False
        elif m == 0:
            for i in range(0,len(A)-1):
                if (A[i] >= A[i+1]):
                    continue
                else:
                    return False
        return True
            
