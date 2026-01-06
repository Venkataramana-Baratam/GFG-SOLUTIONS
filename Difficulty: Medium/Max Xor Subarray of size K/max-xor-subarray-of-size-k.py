class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n = len(arr)
        max_xor = 0
        cur_xor = 0
        for i in range(k):
            
            cur_xor ^=arr[i]
        max_xor = cur_xor
        
        for i in range(k,n):
            
            cur_xor^=arr[i-k]
            cur_xor^=arr[i]
            max_xor = max(max_xor,cur_xor)
        return max_xor
        
       