class Solution:
    def searchMatrix(self, matrix, x):
        for row in matrix:
            row.sort()  
            low = 0
            high = len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == x:
                    return True
                elif row[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
