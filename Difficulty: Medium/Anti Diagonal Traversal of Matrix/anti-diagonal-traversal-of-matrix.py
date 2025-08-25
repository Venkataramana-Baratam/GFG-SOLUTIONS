#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        rows =len(matrix)
        cols =len(matrix[0])
        i = 0
        j  = 0 
        diagonal_index = 0
        res =[]
        while i < rows and j < cols:
            r,c = i,j
            diagonal = []
            while r<rows and c>=0:
                diagonal.append(matrix[r][c])
                r+=1
                c-=1
            res.extend(diagonal)
            diagonal_index+=1
            if j<cols-1:
                j+=1
            else:
                i+=1
        return res