class Solution:
    def maxOnes(self, arr, k):
        # code here
        l = 0
        r =0
        maxi = 0
        n = len(arr)
        zeros = 0 
        while r<n:
            if arr[r]==0:
                zeros+=1
            if zeros>k:
                if arr[l]==0:
                    zeros-=1
                l+=1
                maxi = max(maxi,r-l+1)
            if zeros<=k:
                maxi = max(maxi,r-l+1)
            r+=1
        return maxi