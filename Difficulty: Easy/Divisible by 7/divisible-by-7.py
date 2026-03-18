class Solution:
    def isdivisible7(self, num):
        rem = 0
        
        for ch in num:
            rem = (rem * 10 + int(ch)) % 7
        
        return 1 if rem == 0 else 0