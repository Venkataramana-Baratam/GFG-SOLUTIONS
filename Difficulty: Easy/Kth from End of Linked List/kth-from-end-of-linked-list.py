'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        
        n = 0
        
        temp = head
        
        while temp:
            
            temp = temp.next
            n+=1
            
        need = n - k + 1
        if k>n:
            return -1
            
        temp1 = head
        
        while need>1:
            temp1 = temp1.next
            need-=1
            
        return temp1.data