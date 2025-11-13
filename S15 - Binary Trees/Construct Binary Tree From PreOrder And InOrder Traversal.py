# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIndex = 0
        self.inorderMap = {}
        
        for i in range(len(inorder)):
            self.inorderMap[inorder[i]] = i
        
        return self.buildTreeHelper(preorder, inorder, 0, len(inorder) - 1)

    def buildTreeHelper(self, preorder: List[int], inorder: List[int], inorderStart: int, inorderEnd: int) -> Optional[TreeNode]:
        if inorderStart > inorderEnd:
            return None

        rootValue = preorder[self.preorderIndex]
        root = TreeNode(rootValue)

        rootIndex = self.inorderMap[rootValue]

        self.preorderIndex += 1

        root.left = self.buildTreeHelper(preorder, inorder, inorderStart, rootIndex - 1)
        root.right = self.buildTreeHelper(preorder, inorder, rootIndex + 1, inorderEnd)

        return root

