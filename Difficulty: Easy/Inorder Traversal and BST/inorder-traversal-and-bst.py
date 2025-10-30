class Solution:
    def isRepresentingBST(self, arr, N):
        for i in range(N - 1):
            if arr[i] >= arr[i + 1]:
                return 0
        return 1
