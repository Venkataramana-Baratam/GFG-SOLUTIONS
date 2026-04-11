class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        
        length = 1   
        cnt = 0
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
                cnt += (length - 1)
            else:
                length = 1
        
        return cnt