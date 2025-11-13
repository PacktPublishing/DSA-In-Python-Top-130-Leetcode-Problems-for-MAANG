# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        val = self.f(root)
        return val[0] - 1
    
    def f(self, node):
        if (node is not None):
            left = self.f(node.left)
            right = self.f(node.right)
            
            height = max(left[1], right[1]) + 1
            diameter = max(left[0], right[0], left[1] + right[1] + 1)
            
            return (diameter, height)
            
        else:
            return (0, 0)