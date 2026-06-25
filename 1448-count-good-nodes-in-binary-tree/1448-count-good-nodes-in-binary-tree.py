# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        head = root.val
        count = 1
        def good(node,head):
            if node is None:
                return 0
            if node.val >= head:
                return 1 + good(node.left, node.val) + good(node.right,node.val)
            else:
                return good(node.left, head) + good(node.right,head) 
        return good(root,root.val)
        