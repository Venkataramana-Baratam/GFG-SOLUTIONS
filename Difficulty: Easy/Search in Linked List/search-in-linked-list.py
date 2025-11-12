'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        temp  = head
        while temp:
            
            if key == temp.data:
                return True
            temp = temp.next
        return False