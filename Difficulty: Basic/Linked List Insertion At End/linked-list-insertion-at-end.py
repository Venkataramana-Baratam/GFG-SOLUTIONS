'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        newnode = Node(x)
        if head is None:
            return newnode
        
        temp  =  head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        return head