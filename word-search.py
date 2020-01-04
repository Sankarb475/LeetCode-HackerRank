#solution of https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j, 0):
                    return True
        return False

    def search(self, board, word, i, j, idx):

        if idx == len(word): return True

        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[idx]:
            temp, board[i][j] = board[i][j], '0'
            direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for x, y in direction:
                if self.search(board, word, i + x, j + y, idx + 1): return True
            board[i][j] = temp

        return False
