'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        n = 0
        temp = head
        while temp:
            n+=1
            temp = temp.next
        if k > n or (2*k - 1) == n:
            return head

        dummy1 = head
        dummy2 = head
        x= 0
        y=0
        while x<k-1:
            x+=1
            dummy1 = dummy1.next
        while y<n-k:
            y+=1
            dummy2 = dummy2.next
        dummy1.data, dummy2.data = dummy2.data, dummy1.data
        return head