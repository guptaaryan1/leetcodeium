# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        point, end = dummy, dummy
        if not head.next:
            return None
        for _ in range(n):
            end = end.next
        while end.next:
            point = point.next
            end = end.next
        point.next = point.next.next
        
        

        return dummy.next
        # None      head        1       2       3       4       None
        #                                       point