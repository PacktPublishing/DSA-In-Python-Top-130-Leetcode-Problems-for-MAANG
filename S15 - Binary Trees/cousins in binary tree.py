# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.firstParent = None
        self.secondParent = None
        self.firstLevel =  -1
        self.secondLevel = -1
        
        self.preOrder(root, 0, None, x, y)
        
        return self.firstParent != self.secondParent and self.firstLevel == self.secondLevel
        
    
    def preOrder(self, node, level, parent, x, y):
        if (node is not None):
            if (node.val == x):
                self.firstParent = parent
                self.firstLevel = level
            if (node.val == y):
                self.secondParent = parent
                self.secondLevel = level
            
            if (node.left is not None):
                self.preOrder(node.left, level + 1, node, x, y)
            if (node.right is not None):
                self.preOrder(node.right, level + 1, node, x, y)
        
        