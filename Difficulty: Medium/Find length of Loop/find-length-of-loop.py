'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                cnt = 1
                temp = slow.next
                while temp!=fast:
                    temp = temp.next
                    cnt+=1
                return cnt
        return 0
                
                    