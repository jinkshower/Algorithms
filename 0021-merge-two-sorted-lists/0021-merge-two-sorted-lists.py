# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = list1, list2
        newHead = None
        newTail = None
        while l and r:
            smaller = 0
            if l.val <= r.val:
                # add l to newHead
                smaller = l.val
                l = l.next
            else:
                smaller = r.val
                r = r.next
            newOne = ListNode(smaller)

            if not newHead and not newTail:
                newHead = newOne
                newTail = newHead
            else:
                # insert tail
                newTail.next = newOne
                newTail = newOne
        
        if newTail:
            newTail.next = l if l else r
        else:
            newHead = l if l else r  # 추가!

        return newHead
