
class Solution:
    def diagView(self, mat): 
        n = len(mat)
        res = []
    
 
        for k in range(n):
            i = 0
            j = k
        
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
    
        for k in range(1, n):
            i = k
            j = n - 1
        
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
    
        return res