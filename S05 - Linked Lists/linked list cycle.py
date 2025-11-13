# Definition for singly-linked list.\
# class ListNode:\
#     def __init__(self, x):\
#         self.val = x\
#         self.next = None\
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None or head.next is None):
            return False
        first = head
        second = head.next.next
        while first is not None and second is not None and second.next is not None:
            if (first == second):
                return True
            first = first.next
            second = second.next.next
        return False
