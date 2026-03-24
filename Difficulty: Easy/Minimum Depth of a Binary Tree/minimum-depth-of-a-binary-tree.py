class Solution:
    def minDepth(self, root):
        
        if root is None:
            return 0
            
        # If left child is None, go right
        if root.left is None:
            return 1 + self.minDepth(root.right)
        
        # If right child is None, go left
        if root.right is None:
            return 1 + self.minDepth(root.left)
        
        # If both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))