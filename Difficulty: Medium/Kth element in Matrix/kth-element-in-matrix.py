class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]
            