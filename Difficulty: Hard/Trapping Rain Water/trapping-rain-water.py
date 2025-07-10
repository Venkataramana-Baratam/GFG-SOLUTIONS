
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        prefixmax = [0]*n
        prefixmax[0] = arr[0]
        for i in range(1,n):
            prefixmax[i] = max(prefixmax[i-1],arr[i])
        suffixmax = [0]*n
        suffixmax[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            suffixmax[i] = max(suffixmax[i+1],arr[i])
        total = 0
        for i in range(n):
            leftmax = prefixmax[i] 
            rightmax = suffixmax[i]
            if arr[i]<leftmax and arr[i]<rightmax:
                total += min(leftmax,rightmax)-arr[i]
        return total