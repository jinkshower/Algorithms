# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        self.gather(root1, leaves1)
        self.gather(root2, leaves2)

        return leaves1 == leaves2
        
    def gather(self, node: Optional[TreeNode], leaves: list) -> None:
        if not node:
            return
        
        if not node.left and not node.right:
            leaves.append(node.val)
        
        self.gather(node.left, leaves)
        self.gather(node.right, leaves)