class Solution:
    def findMedian(self, arr):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)

        # Step 2: Find median
        if n % 2 == 1:
            # Odd length → middle element
            return arr[n // 2]
        else:
            # Even length → average of two middle elements
            mid1 = arr[n // 2 - 1]
            mid2 = arr[n // 2]
            return (mid1 + mid2) / 2.0
