# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        answer = [False]  # Using a list to achieve pass-by-reference behavior
    
        def preOrder(node, sumTillParent, targetSum):
            if node:
                sumTillMe = sumTillParent + node.val

                if node.left:
                    preOrder(node.left, sumTillMe, targetSum)
                if node.right:
                    preOrder(node.right, sumTillMe, targetSum)

                if sumTillMe == targetSum and not node.left and not node.right:
                    answer[0] = True

        preOrder(root, 0, targetSum)
        return answer[0]
        
