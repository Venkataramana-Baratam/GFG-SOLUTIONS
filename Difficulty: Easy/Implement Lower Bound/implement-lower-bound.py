class Solution:
    def lowerBound(self, arr, target):
        # code here
        n = len(arr)
        low = 0
        high = n - 1
        
        while low<=high:
            
            mid = (low + high)//2
            
            if arr[mid]>=target:
                high = mid - 1 
            else:
                low = mid + 1
            
        return low
        