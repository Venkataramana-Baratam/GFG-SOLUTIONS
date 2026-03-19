class Solution:
    def findElement(self, arr):
        n = len(arr)
        
       
        leftMax = [0] * n
        leftMax[0] = arr[0]
        
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], arr[i])
        
       
        rightMin = [0] * n
        rightMin[n-1] = arr[n-1]
        
        for i in range(n-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], arr[i])
        
       
        for i in range(1, n-1):
            if leftMax[i] == arr[i] and rightMin[i] == arr[i]:
                return arr[i]
        
        return -1