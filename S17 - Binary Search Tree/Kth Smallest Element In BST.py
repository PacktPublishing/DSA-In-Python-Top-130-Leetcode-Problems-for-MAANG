# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k
        self.inorder(root);
        return self.ans;
    
    def inorder(self, node):
        if (node.left is not None):
            self.inorder(node.left)
        
        self.count += 1
        if (self.count == self.k):
            self.ans = node.val;
            return;
        
        if (node.right is not None):
            self.inorder(node.right);