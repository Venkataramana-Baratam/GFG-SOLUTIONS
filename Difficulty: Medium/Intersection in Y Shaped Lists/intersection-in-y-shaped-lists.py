'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        if head1 is None or head2 is None:
            return None
        
        d1 = head1
        d2 = head2
        
        while d1!=d2:
            d1 =head2 if d1 is None else d1.next
            d2 = head1 if d2 is None else d2.next
        return d1