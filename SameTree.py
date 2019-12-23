# solution of https://leetcode.com/problems/same-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, x: TreeNode, y: TreeNode) -> bool:
        if x and y:
            return x.val == y.val and self.isSameTree(x.left,y.left) and self.isSameTree(x.right,y.right)
        return x==y
                
