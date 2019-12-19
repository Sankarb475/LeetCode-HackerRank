# solution of https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        list1 = []
        for i in range(len(intervals)-1):
            if intervals[i] in list1:
                continue
            for j in range(i+1,len(intervals)):
                if intervals[i][1] >= intervals[j][1]:
                    list1.append(intervals[j])
        print(list1)
        count = 0
        for i in intervals:
            if i not in list1:
                count = count + 1
        return count
            
        
        
