class Solution:
    def transpose(self, mat):
        # code here
        
        
        m = len(mat)
        n = len(mat[0])
        trans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                
                trans[i][j] = mat[j][i]
        return trans