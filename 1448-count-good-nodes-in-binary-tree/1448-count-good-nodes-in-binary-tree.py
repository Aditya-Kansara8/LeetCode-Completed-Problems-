# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(node,head):
            if node is None:
                return 0
            head = max(head, node.val)
            return (head == node.val) + good(node.left, head) + good(node.right,head) 
        return good(root,root.val)
        