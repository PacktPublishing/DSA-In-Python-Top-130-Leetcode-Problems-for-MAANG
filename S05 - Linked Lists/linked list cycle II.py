# Definition for singly-linked list.\
# class ListNode:\
#     def __init__(self, x):\
#         self.val = x\
#         self.next = None\
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        insPoint = None
        while True:
            if (fast is None or fast.next is None):
                return None
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                insPoint = slow
                break
        start = head
        while (start != insPoint):
            start = start.next
            insPoint = insPoint.next
        return start
