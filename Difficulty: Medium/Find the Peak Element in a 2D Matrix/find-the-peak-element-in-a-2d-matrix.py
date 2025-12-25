class Solution:
    def findPeakGrid(self, mat):
        rows, cols = len(mat), len(mat[0])
        left, right = 0, cols - 1

        while left <= right:
            mid_col = (left + right) // 2
            max_row = max(range(rows), key=lambda x: mat[x][mid_col])

            left_val = mat[max_row][mid_col - 1] if mid_col > 0 else float('-inf')
            right_val = mat[max_row][mid_col + 1] if mid_col < cols - 1 else float('-inf')

            if mat[max_row][mid_col] >= left_val and mat[max_row][mid_col] >= right_val:
                return [max_row, mid_col]
            elif left_val > mat[max_row][mid_col]:
                right = mid_col - 1
            else:
                left = mid_col + 1

        return [-1, -1]