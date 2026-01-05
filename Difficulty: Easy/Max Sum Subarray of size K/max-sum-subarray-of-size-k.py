class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        l = 0
        r = 0
        n = len(arr)
        
        cnt = 0
        max_sum = float('-inf')
        ans = 0 
        while r<n:
            ans+=arr[r]
            cnt = (r-l+1)
            if cnt == k:
                max_sum = max(max_sum,ans)
                ans -=arr[l]
                l+=1
            r+=1
        return max_sum