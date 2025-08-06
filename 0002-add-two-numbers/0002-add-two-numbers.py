# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, idx1 = 0, 0
        sum2, idx2 = 0, 0

        while l1:
            sum1 = sum1 + l1.val * (10 ** idx1)
            l1 = l1.next
            idx1 += 1
        
        while l2:
            sum2 = sum2 + l2.val * (10 ** idx2)
            l2 = l2.next 
            idx2 += 1
        
        sum3 = sum1 + sum2 # 807
        if sum3 == 0:
            return ListNode()

        dummy = ListNode(-1)
        res = dummy
        while sum3 > 0:
            val = sum3 % 10
            sum3 = sum3 // 10
            newOne = ListNode(val)
            dummy.next = newOne
            dummy = dummy.next
        
        return res.next
        
