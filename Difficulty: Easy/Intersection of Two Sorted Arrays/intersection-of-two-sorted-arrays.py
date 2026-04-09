class Solution:
    def intersection(self, a, b):
        i, j = 0, 0
        res = []
        
        while i < len(a) and j < len(b):
            
            if a[i] == b[j]:
                
                # Add only distinct elements
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                
                i += 1
                j += 1
            
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        
        return res