# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None

        def successor(node):
            while node.left:
                node = node.left
            return node.val

        node = root.val
        if node < key:
            root.right = self.deleteNode(root.right, key) 
            return root
        if node > key:
            root.left = self.deleteNode(root.left, key) 
            return root
        if node == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            if root.right and root.left:
                successor_val = successor(root.right)
                root.val = successor_val
                root.right = self.deleteNode(root.right, successor_val)
                return root