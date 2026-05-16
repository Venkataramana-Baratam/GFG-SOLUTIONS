#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        #Your code here
        
        
        low = 0 
        high = len(arr) - 1
        
        ans = float("inf")
        while low <= high:
            
            mid = (low + high)//2
            
            if arr[low] <= arr[mid]:
                
                ans = min(ans, arr[low])
                
                low = mid + 1
            else:
                ans = min(ans , arr[mid])
                high = mid - 1
        return ans