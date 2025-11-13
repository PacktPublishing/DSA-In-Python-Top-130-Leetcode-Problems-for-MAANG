# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True
        
        if t1 is None or t2 is None:
            return False
        
        if t1.val != t2.val:
            return False
        
        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
