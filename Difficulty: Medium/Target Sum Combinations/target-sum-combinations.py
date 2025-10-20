class Solution:
    def targetSumComb(self, arr, target):
        # code here
        ds = []
        n = len(arr)
        res = []
        def f(i,ds,target):
            if i==n:
                if target == 0:
                    res.append(ds[:])
                return 
            
            if arr[i]<=target:
                ds.append(arr[i])
                f(i,ds,target-arr[i])
                ds.pop()
            f(i+1,ds,target)
        f(0,ds,target)
        return res