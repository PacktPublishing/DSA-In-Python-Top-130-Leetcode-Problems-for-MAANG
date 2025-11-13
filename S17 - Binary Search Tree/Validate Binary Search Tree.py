# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, None, None)
     
    def isValid(self, node, lower, upper):
        if (node is None):
            return True
        
        if ((lower is not None and node.val < lower) or
            (upper is not None and node.val > upper)):
            return False
        
        return self.isValid(node.left, lower, node.val - 1) and self.isValid(node.right, node.val + 1, upper)
