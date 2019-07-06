# solution of https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heightsSorted = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heightsSorted[i]:
                count = count + 1
        return count
