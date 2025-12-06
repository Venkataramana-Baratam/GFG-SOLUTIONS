#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        
        n = len(arr)
        prefix = [1]*n
        suffix = [1]*n
        
        ans = [1]*n 
        prefix[0] = arr[0]
        for i in range(1,n):
            
            prefix[i] = prefix[i-1] * arr[i]
        suffix[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            
            
            suffix[i] = suffix[i+1] * arr[i]
            
        if n==1:
            
            return [1]
            
        ans[n-1] = prefix[n-2]
        ans[0] = suffix[1]
        
        for i in range(1,n-1):
            
            ans[i] = prefix[i-1] * suffix[i+1]
            
        return ans