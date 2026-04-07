'''
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def areIdentical(self, head1, head2):
        # Code here
        
        while head1 and head2:
            
            if head1.data != head2.data:
                return False
                
            head1 = head1.next
            head2 = head2.next
            
        
        return head1 is None and head2 is None