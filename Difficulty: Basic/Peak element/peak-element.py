class Solution:   
    def peakElement(self,arr):
        # Code here
        maxi  = arr[0]
        k = 0
        for i in range(1,len(arr)):
            if maxi<arr[i]:
                maxi  = arr[i]
                k  = i
        return k