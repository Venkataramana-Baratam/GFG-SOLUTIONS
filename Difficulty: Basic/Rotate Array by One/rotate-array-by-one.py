# User function Template for python3
class Solution:
    def rotate(self, arr):
        if len(arr) == 0:
            return
        last = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
