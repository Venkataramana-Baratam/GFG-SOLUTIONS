#User function Template for python3

class Solution:
    def maxFrequency(self, arr, n, k):
        # Code here
        left = 0
        ans = 0 
        curr = 0
        arr.sort()
        for right in range(len(arr)):
            
            target = arr[right]
            curr+=target
            
            while (right - left+1)*target - curr >k:
                curr -= arr[left]
                left+=1
            ans = max(ans,right - left + 1)
        return ans