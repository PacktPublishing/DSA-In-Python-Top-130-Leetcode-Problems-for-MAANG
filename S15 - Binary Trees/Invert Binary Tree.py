# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)
    
    def invert(self, node):
        if (node is not None):
            left = self.invert(node.left)
            right = self.invert(node.right)
            node.left = right
            node.right = left
        return node
            
        