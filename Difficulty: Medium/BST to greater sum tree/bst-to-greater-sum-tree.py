'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        # code here
        bst = []
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            bst.append(node.data)
            inorder(node.right)
        inorder(root)
        bst.sort(reverse= True)
        
        prefix_sum = {}
        total = 0
        
        for val in bst:
            prefix_sum[val] = total
            total+=val
        def update(node):
            if node is None:
                return 
            update(node.left)
            node.data = prefix_sum[node.data]
            update(node.right)
            
        update(root)
        return root