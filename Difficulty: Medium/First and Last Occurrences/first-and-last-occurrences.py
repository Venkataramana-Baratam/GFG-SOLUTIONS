class Solution:
    def find(self, arr, x):
        n = len(arr)
        result = [-1, -1]

        # First occurrence
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                if arr[mid] == x:
                    result[0] = mid
                high = mid - 1
            else:
                low = mid + 1

        # Last occurrence
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                if arr[mid] == x:
                    result[1] = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
