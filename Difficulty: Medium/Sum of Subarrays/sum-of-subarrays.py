class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total = 0
        for i in range(n):
            total += arr[i] * (i + 1) * (n - i)
        return total
