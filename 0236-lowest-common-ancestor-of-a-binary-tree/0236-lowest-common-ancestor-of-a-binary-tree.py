# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node is None:
                return None
            if node == p or node == q:
                return node
            
            left = lca(node.left)
            right = lca(node.right)

            if left is not None and right is not None:
                return node
            elif left is not None and right is None:
                return left
            elif right is not None and left is None:
                return right
        return lca(root) 
