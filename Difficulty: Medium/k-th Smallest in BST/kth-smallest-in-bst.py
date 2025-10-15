'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        # code here
        
        res =[]
        def inorder(node):
            
            if node is None:
                return
            inorder(node.left)
            res.append(node.data)
            inorder(node.right)
        inorder(root)
        #print(res)
        if 0 < k <= len(res):
            return res[k - 1]
        else:
            return -1
