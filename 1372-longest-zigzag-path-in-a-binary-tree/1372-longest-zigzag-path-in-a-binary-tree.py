# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # 한노드에서 깊이 탐색 - > dfs
        # 기억해야 하는 정보 ?
        # 현재 노드, 지금까지 zig zag한 길이 , 방금 왼쪽 오른쪽 ?
        self.max_len = 0

        def dfs(node, is_left, length):
            if not node:
                return
            
            self.max_len = max(self.max_len, length)

            if is_left:
                dfs(node.right, False, length + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, length + 1)
                dfs(node.right, False, 1)
            
            #우리는 max_len을 갱신해야 한다. 

        dfs(root.left, True, 1)
        dfs(root.right, False, 1)

        return self.max_len