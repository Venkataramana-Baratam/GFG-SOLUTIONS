class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        
        
        arr.sort()
        
        total = 0
        
        n = len(arr)
        
        i = n - 1
        
        while i > 0:
            
            if (arr[i] - arr[i - 1]) < k:
                
                total += arr[i] + arr[i - 1]
                
                i -= 2
            else:
                i-=1
        return total