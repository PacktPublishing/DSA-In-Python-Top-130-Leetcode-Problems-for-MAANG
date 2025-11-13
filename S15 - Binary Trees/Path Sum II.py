# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []
        path = []
        
        self.preOrder(root, 0, path, targetSum)
        
        return self.answer;
    
    def preOrder(self, node, sumTillParent, pathTillParent, targetSum):
        if (node is not None):
            sumTillMe = sumTillParent + node.val
            pathTillParent.append(node.val)
            
            if (node.left is None and node.right is None and sumTillMe == targetSum):
                path = []
                for num in pathTillParent:
                    path.append(num)
                self.answer.append(path)
            
            if (node.left is not None):
                self.preOrder(node.left, sumTillMe, pathTillParent, targetSum)
                
            if (node.right is not None):
                self.preOrder(node.right, sumTillMe, pathTillParent, targetSum)
            
            pathTillParent.pop()
            
