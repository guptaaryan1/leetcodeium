# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        powof10 = 1
        cur = l1
        s = 0
        while cur:
            s += cur.val * (10 ** powof10)
            powof10 += 1
            cur = cur.next
        powof10 = 1
        cur = l2
        while cur:
            s += cur.val * (10 ** powof10)
            powof10 += 1
            cur = cur.next
        if s == 0: return ListNode(0)
        head = ListNode(0, None)
        cur = head

        while s > 0:
            cur.next = ListNode(s % 10)
            s //= 10
            cur = cur.next
        return head.next.next


        