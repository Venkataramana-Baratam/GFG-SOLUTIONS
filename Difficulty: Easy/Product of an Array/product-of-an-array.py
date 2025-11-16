class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        ans = 1
        for i in arr:
            ans*=i
        return ans%1000000007