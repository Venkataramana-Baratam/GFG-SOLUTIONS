class Solution:
    def thirdLargest(self,arr):
        # code here
        
        n = len(arr)
        if n<3:
            return -1
        arr.sort(reverse = True)
        return arr[2]