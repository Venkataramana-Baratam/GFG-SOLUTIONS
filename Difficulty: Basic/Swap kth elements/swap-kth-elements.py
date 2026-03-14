class Solution:
    def swapKth(self, arr, k):
        
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        
        return arr
