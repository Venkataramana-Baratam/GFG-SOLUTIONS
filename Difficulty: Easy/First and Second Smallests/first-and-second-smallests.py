class Solution:
    def minAnd2ndMin(self, arr):
        if len(arr) < 2:
            return [-1]
        
        first = second = float('inf')
        
        for num in arr:
            if num < first:
                second = first
                first = num
            elif first < num < second:  # strictly greater than first and smaller than second
                second = num
        
        if second == float('inf'):
            return [-1]
        return [first, second]
