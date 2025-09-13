'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)
        zero = zero_head
        one = one_head
        two = two_head
        temp = head
        while temp:
            if temp.data==0:
                zero.next = temp
                zero = temp
            elif temp.data==1:
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next 
        two.next = None
        new_head = zero_head.next
        return new_head