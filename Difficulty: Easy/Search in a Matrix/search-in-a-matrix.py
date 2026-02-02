class Solution:
    def searchMatrix(self, matrix, x):
        
        def bin(arr):
            arr.sort()
            low = 0
            high = len(arr) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    return True
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        for mat in matrix:
            if bin(mat):
                return True
        
        return False
