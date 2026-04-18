class Solution:
    def maxOnes(self, arr):
        total_ones = sum(arr)
        
        max_sum = float('-inf')
        curr_sum = 0
        
        for x in arr:
            
            val = 1 if x == 0 else -1
            
            curr_sum = max(val, curr_sum + val)
            max_sum = max(max_sum, curr_sum)
        
        
        if max_sum < 0:
            return total_ones
        
        return total_ones + max_sum