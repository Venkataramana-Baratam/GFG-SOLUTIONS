class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMedian(self, root):
        res = []
        
        # Inorder traversal (sorted order)
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.data)
            inorder(node.right)
        
        inorder(root)
        n = len(res)
        
        # If odd, return middle element
        if n % 2 == 1:
            return res[n // 2]
        # If even, return n/2-th element (1-based index → (n//2 - 1) for 0-based)
        else:
            return res[(n // 2) - 1]
