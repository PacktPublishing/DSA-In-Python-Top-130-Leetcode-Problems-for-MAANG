# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = self.findLength(head)
        if (n == 1):
            return True
        
        reversePoint = n//2
        if (n%2 == 1):
            reversePoint = (n//2) + 1
        
        head2 = self.findNodeAtPos(head, reversePoint)
        prev = self.findNodeAtPos(head, reversePoint - 1)
        
        self.reverse(head2, prev)
        first = head
        second = prev.next
        
        while (first is not None and second is not None):
            if (first.val != second.val):
                return False
            first = first.next
            second = second.next
        
        return True
    
    def findLength(self, head):
        length = 0
        curr = head
        while (curr is not None):
            length += 1
            curr = curr.next
        return length

    def findNodeAtPos(self, head, pos):
        count = 0
        curr = head
        while (count < pos):
            count += 1
            curr = curr.next
        return curr
    
    def reverse(self, head, prev):
        a = head
        b = head.next
        while (a is not None and b is not None):
            temp = b.next
            b.next = a
            a = b
            b = temp
        head.next = None
        prev.next = a
    