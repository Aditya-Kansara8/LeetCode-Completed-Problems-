# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l = []
        r = []
        def leaf(node, l):
            if node.left is None and node.right is None:
                l.append(node.val)
            if node.left is not None:
                leaf(node.left,l)
            if node.right is not None:
                leaf(node.right,l)
        leaf(root1, l)
        leaf(root2, r)
        return l == r
