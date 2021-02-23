# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lis = []
        cur = head
        while cur is not None:
            lis.append(cur.val)
            cur = cur.next
        return lis == lis[::-1]
        