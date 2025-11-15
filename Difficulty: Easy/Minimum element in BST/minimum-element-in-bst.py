"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        # code here
        res = []
        def preorder(node):
            if node is None:
                return 
            preorder(node.left)
            res.append(node.data)
            preorder(node.right)
        preorder(root)
        return min(res)