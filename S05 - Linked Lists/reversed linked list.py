# Definition for singly-linked list.\
# class ListNode:\
#     def __init__(self, val=0, next=None):\
#         self.val = val\
#         self.next = next\
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.newHead = None
        if (head is not None):
            lastNode = self.reverse(head)
            lastNode.next = None
        return self.newHead
    def reverse(self, current):
        if (current.next is None):
            self.newHead = current
            return current
        else:
            lastNode = self.reverse(current.next)
            lastNode.next = current
            return current
