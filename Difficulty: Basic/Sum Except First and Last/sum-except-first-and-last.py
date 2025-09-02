class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        #code here
        ans = 0
        n = len(arr)
        for i in range(1,n-1):
            ans+=arr[i]
        return ans