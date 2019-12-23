# Solution of https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(r,c):
            image[r][c]= newColor
            for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=x<len(image) and 0<=y<len(image[0]) and image[x][y] == oldcolor:
                    dfs(x,y)
        
        oldcolor = image[sr][sc]
        if oldcolor != newColor:
            dfs(sr,sc)
        return image
            
            
