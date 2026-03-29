from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []

    
        q = deque()
        q.append((root, 0))

    
        hd_map = {}

        while q:
            node, hd = q.popleft()

            
            if hd not in hd_map:
                hd_map[hd] = node.data

            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        
        result = []
        for hd in sorted(hd_map):
            result.append(hd_map[hd])

        return result