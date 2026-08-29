# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        p = 0
        while l1:
            s += (l1.val) * (10 ** p)
            l1 = l1.next
            p += 1
        p = 0
        while l2:
            s += (l2.val) * (10 ** p)
            l2 = l2.next
            p += 1
        
        dummy = node = ListNode()
        if s == 0:
            return ListNode(0)
        while s > 0:
            newNode = ListNode(s % (10))
            node.next = newNode
            node = node.next
            s //= 10
        return dummy.next