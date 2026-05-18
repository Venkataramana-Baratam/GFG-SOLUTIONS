class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        
        res = bin(n)[2::]
        return res == res[::-1]