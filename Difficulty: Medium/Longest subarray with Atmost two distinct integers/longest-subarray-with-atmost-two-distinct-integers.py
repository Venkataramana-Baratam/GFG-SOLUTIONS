class Solution:
    def totalElements(self, arr):
        
        n = len(arr)
        l = 0
        maxi = 0
        mpp = {}
        
        for r in range(n):
            
            mpp[arr[r]] = mpp.get(arr[r], 0) + 1
            
            while len(mpp) > 2:
                mpp[arr[l]] -= 1
                
                if mpp[arr[l]] == 0:
                    del mpp[arr[l]]
                
                l += 1
            
            maxi = max(maxi, r - l + 1)
        
        return maxi