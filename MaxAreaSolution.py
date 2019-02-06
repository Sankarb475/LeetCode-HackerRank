# solution of https://leetcode.com/problems/container-with-most-water/

# O(n) solution

class MaxAreaSolution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, i, j = 0, 0, len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                less = height[i]
                i += 1
            else:
                less = height[j]
                j -= 1
            new = (j - i + 1) * less
            if new > area:
                area = new
        return area
    
    
# O(n^2) solution

class MaxAreaSolution:
    def maxArea(self, height: 'List[int]') -> 'int':
        a = []
        for i in range(len(height)):
            a.append([i,height[i]])
        b = []   
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                b.append(abs((a[i][0] - a[j][0])*(min(a[i][1],a[j][1]))))
        return max(b)
    
    
 # another way to solve this, O(n^2) solution

class MaxAreaSolution:
    def maxArea(self, height: 'List[int]') -> 'int':
        b = []
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                b.append(abs((j-i)*(min(height[i], height[j]))))
        return max(b)
