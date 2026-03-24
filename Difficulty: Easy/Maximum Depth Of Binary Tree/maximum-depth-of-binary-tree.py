#User function Template for python3


class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    def maxDepth(self, root):
        pass
        
        
        if root is None:
            return 0
            
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return 1 + max(l,r)