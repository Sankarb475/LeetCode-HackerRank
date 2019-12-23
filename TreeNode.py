# solution of https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth = 0
        print(root)
        def dfs(root, depth):
            if not root: return
            if not root.left and not root.right:
                self.maxDepth = max(self.maxDepth,depth)
            if root.left: 
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)
        dfs(root,1)
        return self.maxDepth
