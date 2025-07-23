from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([(root, root.val, [root.val])])
        while queue:
            node, current_sum, path = queue.popleft()
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path)
            if node.left:
                queue.append((node.left, current_sum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, current_sum + node.right.val, path + [node.right.val]))
        return result


        