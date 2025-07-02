# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val == val:
            return root

        def dfs(node, val):
            if not node:
                return None
            
            if node.val == val:
                return node
            
            left = dfs(node.left, val)
            right = dfs(node.right, val)

            return left or right

        node = dfs(root, val)
        return node