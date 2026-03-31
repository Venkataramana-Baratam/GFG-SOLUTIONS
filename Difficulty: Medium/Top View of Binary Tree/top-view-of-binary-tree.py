'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
        
class Solution:
    def topView(self, root):
        # code here
        
        
        if root is None:
            return None
            
        todo = deque()
        
        todo.append((root,0))
        
        mpp = {}
        
        while todo:
            
            node,x = todo.popleft()
            
            if x not in mpp:
                
                mpp[x] = node.data
            if node.left:
                
                todo.append((node.left,x-1))
                
            if node.right:
                todo.append((node.right,x+1))
                
        ans = []
        
        for i in sorted(mpp):
            
            ans.append(mpp[i])
            
        return ans
        
        