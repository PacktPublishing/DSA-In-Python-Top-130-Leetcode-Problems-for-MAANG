# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []
        q = deque()
        q.append((root, 1))
        
        answer = []
        
        while (len(q) > 0):
            (node, level) = q[0]
            q.popleft()
            
            if (len(answer) < level):
                answer.append([])
            answer[-1].append(node.val)
            
            if (node.left is not None):
                q.append((node.left, level + 1))
            
            if (node.right is not None):
                q.append((node.right, level + 1))
        
        return answer
            
            