class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        
        ans = []
        
        for l, r in queries:
            total = prefix[r+1] - prefix[l]
            length = r - l + 1
            
            ans.append(total // length)
        
        return ans