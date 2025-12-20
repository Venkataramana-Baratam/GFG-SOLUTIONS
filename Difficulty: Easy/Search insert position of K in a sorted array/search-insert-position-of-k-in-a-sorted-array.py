class Solution:
    def searchInsertK(self, arr, k):
        # code here
        n = len(arr)
        for i in range(n-1):
            
            if arr[i]==k:
                return i
            
        dummy = arr[:]
        dummy.append(k)
        dummy.sort()
        for i in range(len(dummy)):
            
            if dummy[i]==k:
                return i