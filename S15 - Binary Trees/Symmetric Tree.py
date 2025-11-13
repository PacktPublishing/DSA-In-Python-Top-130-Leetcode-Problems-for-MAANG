# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSym(root.left, root.right)
    
    def isSym(self, f1, f2):
        if (f1 is None and f2 is None):
            return True
        if (f1 is None or f2 is None):
            return False
        
        return f1.val == f2.val and self.isSym(f1.left, f2.right) and self.isSym(f1.right, f2.left)