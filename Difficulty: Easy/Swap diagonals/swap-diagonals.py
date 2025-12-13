class Solution:
    def swapDiagonal(self, mat):
        
        
        res = []
        
        minor = []
        major = []
        m = len(mat)
        n = len(mat[0])
        for i in range(len(mat)):
            minor.append(mat[i][i])
            major.append(mat[i][n-1-i])
        
        for i in range(m):
            mat[i][i] = major[i]
        for j in range(n):
            mat[j][n-j-1] = minor[j]
        
        return mat