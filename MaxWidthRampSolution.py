# solution of https://leetcode.com/problems/maximum-width-ramp/     ==> medium






class MaxWidthRampSolution:
    def maxWidthRamp(self, a):
        a = sorted([(x, i) for i, x in enumerate(a)])        
        ans, min_i = 0, float('inf')   
        for x, i in a:
            min_i = min(i, min_i)
            print(min_i)
            ans = max(ans, i - min_i)
        return ans





# 94/98 test cases passed, due to memory limit exceeded error

class MaxWidthRampSolution:
    def maxWidthRamp(self, A: 'List[int]') -> 'int':
        listOut = []
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i] <= A[j]:
                    listOut.append(j-i)
        if len(listOut) == 0:
            return 0
        return max(listOut)
