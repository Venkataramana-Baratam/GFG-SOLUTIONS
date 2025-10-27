class Solution:
    def subsetSums(self, arr):
        # code here
        res = []
        ds = []
        n = len(arr)
        
        def f(i, ds, s):
            if i == n:
                res.append(s)
                return
            
            ds.append(arr[i])
            s += arr[i]
            f(i + 1, ds, s)
            
            ds.pop()
            s -= arr[i]
            
            f(i + 1, ds, s)
        
        f(0, ds, 0)
        return res
