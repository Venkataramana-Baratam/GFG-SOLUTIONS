# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    if x == 1:
        return head.next  
    temp = head
    for i in range(1, x - 1):
        if temp is None or temp.next is None:
            return head  
        temp = temp.next
    if temp.next:
        temp.next = temp.next.next  
    return head
