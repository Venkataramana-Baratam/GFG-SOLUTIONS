'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        # code here
        
        
        def merge2lists(l1,l2):
            
            dummyNode = Node(-1)
            
            res = dummyNode
            
            while l1 and l2:
                
                if l1.data<l2.data:
                    
                    res.bottom = l1
                    
                    l1 = l1.bottom
                    
                else:
                    
                    res.bottom = l2
                    l2 = l2.bottom
                    
                res = res.bottom
                res.next = None
                
            if l1:
                res.bottom = l1
            else:
                res.bottom = l2
                
            return dummyNode.bottom
            
        
        if root is None or root.next is None:
            
            return root
        
        
        mergedhead = self.flatten(root.next)
        
        root = merge2lists(root,mergedhead)
        
        return root
        