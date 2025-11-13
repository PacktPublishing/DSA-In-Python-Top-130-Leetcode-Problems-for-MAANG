# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.preOrder(root, False)
        return self.sum
    
    def preOrder(self, node, leftChild):
        if (node is not None):
            if (node.left is None and node.right is None and leftChild == True):
                self.sum += node.val
            if (node.left is not None):
                self.preOrder(node.left, True)
            if (node.right is not None):
                self.preOrder(node.right, False)
