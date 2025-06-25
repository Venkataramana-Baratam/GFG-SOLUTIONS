class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        nodeSet = set()
        prev = None
        while head:
            if head in nodeSet:
                prev.next = None  # Loop removed
                return
            nodeSet.add(head)
            prev = head
            head = head.next
