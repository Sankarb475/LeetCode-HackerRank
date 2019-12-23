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
                
       
    
    
    
        
#Another solution 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, x: TreeNode, y: TreeNode) -> bool:
        od1 = self.preorder(x,[])
        od2 = self.preorder(y,[])
        if od1 == od2:
            return True
        return False
    
    def preorder(self, root:TreeNode, order):
        if not root:
            return order
        
        order.append(root.val)
        
        if root.left:
            self.preorder(root.left, order)
        else:
            order.append(None)
            
        if root.right:
            self.preorder(root.right, order)
        else:
            order.append(None)
        
        return order
        
            
        
