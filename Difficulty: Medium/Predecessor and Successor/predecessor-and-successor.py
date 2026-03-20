class Solution:
    def findPreSuc(self, root, key):
        res = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node)   
            inorder(node.right)
        
        inorder(root)
        
        def lower_bound(arr, target):
            low, high = 0, len(arr)
            
            while low < high:
                mid = (low + high) // 2
                
                if arr[mid].data < target:   
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        def upper_bound(arr, target):
            low, high = 0, len(arr)
            
            while low < high:
                mid = (low + high) // 2
                
                if arr[mid].data <= target:  
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        lb = lower_bound(res, key)
        ub = upper_bound(res, key)
        
        
        pre = res[lb - 1] if lb > 0 else None
        suc = res[ub] if ub < len(res) else None
        
        return pre, suc