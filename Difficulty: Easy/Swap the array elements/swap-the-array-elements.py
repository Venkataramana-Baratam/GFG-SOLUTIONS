class Solution:
    def swapElements(self, arr):
        n = len(arr)

        for i in range(n - 2):
            arr[i], arr[i + 2] = arr[i + 2], arr[i]

        return arr
