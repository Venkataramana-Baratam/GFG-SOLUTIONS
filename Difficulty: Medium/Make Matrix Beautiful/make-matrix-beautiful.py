class Solution:
    def balanceSums(self, mat):
        # code here
        total_sum = 0
        row_sum = [0]*len(mat)
        column_sum = [0]*len(mat)
        target_sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                total_sum+=mat[i][j]
                column_sum[j]+=mat[i][j]
                row_sum[i]+=mat[i][j]
        target_sum = max(max(row_sum),max(column_sum))
        desired_sum = target_sum*len(mat) - total_sum
        return desired_sum