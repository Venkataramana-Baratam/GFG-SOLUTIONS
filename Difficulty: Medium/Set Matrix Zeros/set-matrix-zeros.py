class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        
        m = len(mat)
        n = len(mat[0])
        row = [0]*m
        column = [0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    row[i] = 1
                    column[j] =1
        for k in range(m):
            for l in range(n):
                if row[k] or column[l]:
                    mat[k][l]=0
        