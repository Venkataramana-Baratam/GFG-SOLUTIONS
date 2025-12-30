'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
''''''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoLists(self, head1, head2):

        # Step 1: Reverse both lists
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        head = None
        tail = None

        # Step 2: Add digits with carry
        while head1 or head2 or carry:
            s = carry

            if head1:
                s += head1.data
                head1 = head1.next

            if head2:
                s += head2.data
                head2 = head2.next

            carry = s // 10
            node = Node(s % 10)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        
        head = self.reverse(head)

        while head and head.data == 0 and head.next:
            head = head.next

        return head
