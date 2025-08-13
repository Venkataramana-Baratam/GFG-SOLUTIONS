class Solution:
    def isPowerof3(self, N):
        if N <= 0:
            return "No"
        while N % 3 == 0:
            N //= 3
        return "Yes" if N == 1 else "No"
