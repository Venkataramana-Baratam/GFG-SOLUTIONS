class Solution:
    def findMin(self, arr):
        # code here
        
        ans = float('inf')
        
        low = 0
        high = len(arr) - 1
        
        while low<=high:
            
            mid = (low + high) // 2
            
            if arr[low] <= arr[mid]:
                
                ans = min(ans,arr[low])
                low = mid + 1
                
            else:
                
                ans = min(ans, arr[mid])
                
                high = mid - 1
                
        return ans