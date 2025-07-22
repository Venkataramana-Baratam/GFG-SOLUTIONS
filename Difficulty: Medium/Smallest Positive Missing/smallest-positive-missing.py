import sys

class Solution:
    def missingNumber(self, arr):
        arr.sort()
        n = len(arr)
        smallest_missing = 1  
        for num in arr:
            if num == smallest_missing:
                smallest_missing += 1
            elif num > smallest_missing:
                break  
        return smallest_missing
