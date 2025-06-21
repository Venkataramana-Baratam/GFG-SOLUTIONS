class Solution:
    
    # Function to rotate a linked list to the left by k nodes.
    def rotate(self, head, k):
        if head is None or head.next is None:
            return head

        # Step 1: Count number of nodes
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1

        # Step 2: Normalize k
        k = k % n
        if k == 0:
            return head

        # Step 3: Move temp1 to the (k-1)th node
        temp1 = head
        for _ in range(k - 1):
            temp1 = temp1.next

        # Step 4: Set new head and cut the list
        new_head = temp1.next
        temp1.next = None

        # Step 5: Move to the end of new_head part
        temp2 = new_head
        while temp2.next:
            temp2 = temp2.next

        # Step 6: Attach old head at the end
        temp2.next = head

        return new_head
