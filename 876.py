# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        def middleNode(self, head):
            hare= tor = head
            if head is not None:
                while hare is not None and hare.next is not None:
                    tor = tor.next
                    hare = hare.next.next
                return tor