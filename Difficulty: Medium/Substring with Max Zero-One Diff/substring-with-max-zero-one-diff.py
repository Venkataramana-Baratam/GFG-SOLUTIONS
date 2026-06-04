class Solution:
    def maxSubstring(self, s):
        curr_sum = 0
        max_sum = float('-inf')

        for ch in s:
            val = 1 if ch == '0' else -1

            curr_sum = max(val, curr_sum + val)
            max_sum = max(max_sum, curr_sum)

        return -1 if max_sum < 0 else max_sum