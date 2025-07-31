'''
    # Node Class
    class Node:
		 def __init__(self, data):
    		 self.data = data
    		 self.next = None
	
'''

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None