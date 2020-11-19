# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        total = 0
        while l1 or  l2 or total>0:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            l3.next = ListNode(total%10)
            l3 = l3.next
            total //= 10

        return head.next
        

      