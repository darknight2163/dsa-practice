# File: reverse_linked_list.py
# Problem: Reverse a singly linked list and return the new head.
# Approach: Use two pointers, prev and curr. Reverse the next pointer
#           of each node one by one while traversing the linked list.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev