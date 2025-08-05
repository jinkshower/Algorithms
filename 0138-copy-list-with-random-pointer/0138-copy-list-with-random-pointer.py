"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. 원본 노드 → 복사 노드 맵핑
        old_to_new = {}

        # 1차 루프: 노드 복사만 먼저 (next/random 처리 X)
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_new[cur] = copy
            cur = cur.next

        # 2차 루프: next / random 포인터 복사
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new.get(cur.next)
            copy.random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]


