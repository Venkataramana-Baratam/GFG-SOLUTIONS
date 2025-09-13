"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        
        tail = head
        while tail.next:
            tail = tail.next
        current = head
        while current:
            nextnode = current.next
            current.next = current.prev
            current.prev = nextnode
            current = nextnode
        current = head
        head = tail
        tail  = current
        return head