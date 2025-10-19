'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getKClosest(self, root, target, k):
        res = []
        ans = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.data)
            inorder(node.right)
        inorder(root)
        res.sort(key=lambda x: abs(target - x))
        
        for i in range(k):
            ans.append(res[i])

        return ans

            
            