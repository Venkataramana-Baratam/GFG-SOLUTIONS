class Solution:
    def diagonalSort(self, matrix, n, m):
        def diag(r, c, order=True):
            i, j = r, c
            diagonal = []
            while i < n and j < m:
                diagonal.append(matrix[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse= order)
            i, j = r, c
            for val in diagonal:
                matrix[i][j] = val
                i += 1
                j += 1
        for i in range(1,n):
            diag(i, 0, order=False)
        for j in range(1, m):
            diag(0, j, order=True)
        
        return matrix
