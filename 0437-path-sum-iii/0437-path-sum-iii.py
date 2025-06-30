
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        # 현재 노드에서 시작하는 경로 개수
        def dfs(node, curr_sum):
            if not node:
                return 0
            count = 1 if curr_sum + node.val == targetSum else 0
            count += dfs(node.left, curr_sum + node.val)
            count += dfs(node.right, curr_sum + node.val)
            return count

        return (
            dfs(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
