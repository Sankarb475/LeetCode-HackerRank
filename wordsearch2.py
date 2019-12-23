# solution of https://leetcode.com/problems/word-search/

#DFS solution 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        self.Nrows, self.Ncols = len(board), len(board[0])
        
        for r in range(self.Nrows):
            for c in range(self.Ncols):
                if board[r][c] == word[0] and self.dfs(board,r,c,0, word):
                    return True
        return False
    
    def dfs(self,board,i,j,idx,target):
        if idx == len(target):
            return True
        
        if i<0 or i> len(board)-1 or j<0 or j>len(board[0])- 1 or board[i][j]!=target[idx]:
            return False
        
        original = board[i][j]
        board[i][j] = ""
        
        if self.dfs(board,i+1,j,idx+1, target) or self.dfs(board,i-1,j,idx+1,target) or self.dfs(board,i,j+1,idx+1,target) or self.dfs(board,i,j-1,idx+1,target):
            return True
        else:
            board[i][j] = original
            
        
