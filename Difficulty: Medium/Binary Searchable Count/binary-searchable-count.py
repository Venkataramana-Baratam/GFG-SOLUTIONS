class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        count = 0

        def bin_search(num):
            nonlocal count

            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2

                if arr[mid] == num:
                    count += 1
                    return

                elif arr[mid] < num:
                    l = mid + 1

                else:
                    r = mid - 1

        for num in arr:
            bin_search(num)

        return count