class Solution:
    def KthMissingElement(self, arr, k):
        n = len(arr)
        for i in range(1, n):
            gap = arr[i] - arr[i-1] - 1
            if k <= gap:
                return arr[i-1] + k
            k -= gap
        return -1
