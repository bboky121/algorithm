#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        lists = set()
        while head:
            if head in lists:
                return True
            else:
                lists.add(head)
                head = head.next
        return False
