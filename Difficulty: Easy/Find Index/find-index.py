class Solution:
    def findIndex(self, arr, key):
        start = -1
        end = -1

        for i in range(len(arr)):
            if arr[i] == key:
                if start == -1:
                    start = i
                end = i

        return [start, end]
