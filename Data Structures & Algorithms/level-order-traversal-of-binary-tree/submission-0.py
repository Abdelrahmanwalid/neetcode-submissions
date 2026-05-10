# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [[]]
        if not root:
            return []

        queue = deque([(root, 0)])

        while queue:
            node, index = queue.popleft()

            if node.left:
                queue.append((node.left, index + 1))
            if node.right:
                queue.append((node.right,index + 1))
            if index > len(result) - 1:
                result.append([])
            result[index].append(node.val)
        return result

