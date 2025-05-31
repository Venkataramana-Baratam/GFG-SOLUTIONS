class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])  
        def upper_bound(row, x):
            low, high = 0, len(row)
            while low < high:
                mid = (low + high) // 2
                if row[mid] <= x:
                    low = mid + 1
                else:
                    high = mid
            return low 

        def countsmall(mat, x):
            cnt = 0
            for row in mat:
                cnt += upper_bound(row, x)
            return cnt

        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        req = (n * m) // 2

        while low <= high:
            mid = (low + high) // 2
            small_equal = countsmall(mat, mid)
            if small_equal <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low
