class Solution:
    def findSubsets(self, arr):
        # code here
        arr.sort()
        ans = set()
        n = len(arr)
        ds = []
        def f(i):
            
            if i==n:
                ans.add(tuple(ds))
                return 
            ds.append(arr[i])
            f(i+1)
            ds.pop()
            f(i+1)
        f(0)
        
        res = [list(t) for t in ans]
        return res