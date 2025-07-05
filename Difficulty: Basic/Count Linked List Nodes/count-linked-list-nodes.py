'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        temp = head
        cnt= 1
        while temp and temp.next:
            temp = temp.next
            cnt+=1
        return cnt