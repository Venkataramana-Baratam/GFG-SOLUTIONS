'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        
        if root is None:
            return None
        mpp = {}
        todo = deque()
        
        todo.append((root,0))
        
        while todo:
            
            node,x = todo.popleft()
            
            
            mpp[x] = node.data
            
            
            if node.left:
                
                todo.append((node.left,x-1))
            
            if node.right:
                
                todo.append((node.right,x+1))
                
        
        res = []
        
        for i in sorted(mpp):
            res.append(mpp[i])
            
        return res