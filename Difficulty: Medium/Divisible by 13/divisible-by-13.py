class Solution:
    def divby13(self, s):
        rem = 0
        for ch in s:
            rem = (rem * 10 + int(ch)) % 13
        return rem == 0
