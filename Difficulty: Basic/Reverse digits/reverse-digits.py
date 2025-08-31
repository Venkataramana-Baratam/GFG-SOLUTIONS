# User function Template for python3

class Solution:
    def reverseDigits(self, n):
        # Convert to string, reverse using slicing, then convert back
        y = str(n)
        res = y[::-1]
        return int(res)
