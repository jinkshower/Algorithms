# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        cur_level = 1
        max_level = 1
        max_sum = float('-inf')
        q = collections.deque([root])

        while q:
            qLen = len(q)
            level_sum = 0

            for i in range(qLen):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = cur_level
            cur_level += 1
        
        return max_level

