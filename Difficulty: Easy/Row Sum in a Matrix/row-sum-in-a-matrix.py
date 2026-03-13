class Solution:
    def rowSum(self, mat):
        # Code here
        res = []
        for num in mat:
            cnt = 0

            for i in range(len(num)):
               cnt+=num[i]
            res.append(cnt)
        return res