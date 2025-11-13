# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.countNodes(root, float('-inf'))
        return self.count

    def countNodes(self, node: TreeNode, maxTillParent: int) -> None:
        if node is not None:
            maxTillMe = node.val
            if maxTillParent == float('-inf'):
                self.count += 1
            else:
                if node.val >= maxTillParent:
                    self.count += 1
                maxTillMe = max(maxTillMe, maxTillParent)
            self.countNodes(node.left, maxTillMe)
            self.countNodes(node.right, maxTillMe)

        
