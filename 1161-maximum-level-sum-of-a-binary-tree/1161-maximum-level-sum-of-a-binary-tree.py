# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        smax = None
        total = l = result = 0
        while queue:
            level_size = len(queue)
            total = 0
            l += 1
            for i in range(level_size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if smax is None or total > smax:
                result = l
                smax = total
        return result