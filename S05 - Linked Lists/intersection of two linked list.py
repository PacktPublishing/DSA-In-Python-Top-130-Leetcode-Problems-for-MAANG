# Definition for singly-linked list.\
# class ListNode:\
#     def __init__(self, x):\
#         self.val = x\
#         self.next = None\

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = self.findLength(headA)
        n = self.findLength(headB)
        fp = headA
        sp = headB
        if (m <= n):
            for i in range(n - m):
                sp = sp.next
        else:
            for i in range(m - n):
                fp = fp.next
        while fp is not None:
            if (fp == sp):
                return fp
            fp = fp.next
            sp = sp.next
        return None
    def findLength(self, head):
        length = 0
        curr = head
        while (curr is not None):
            curr = curr.next
            length += 1
        return length
