'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        def reverse_linked_list(head):
            if head is None or head.next is None:
                return head
            new_node = reverse_linked_list(head.next)
            front =head.next
            front.next = head
            head.next = None
            return new_node
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        new_head = reverse_linked_list(slow.next)
        first = head
        second = new_head
        while second is not None:
            if first.data!=second.data:
                reverse_linked_list(new_head)
                return False
            first = first.next
            second = second.next
        reverse_linked_list(new_head)
        return True