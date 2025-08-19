class Solution:
    def farMin(self, arr):
        n = len(arr)
        suffix_min = [0]*n
        suffix_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], arr[i])
        res = [-1]*n
        for i in range(n):
            low, high = i+1, n-1
            ans = -1
            while low <= high:
                mid = (low + high)//2
                if suffix_min[mid] < arr[i]:
                    ans = mid
                    low = mid + 1   
                else:
                    high = mid - 1
            res[i] = ans
        return res
