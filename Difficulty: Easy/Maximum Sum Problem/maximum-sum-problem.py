class Solution:
    def maxSum(self, n):
        
        dp = {}
        
        def solve(num):
            if num == 0:
                return 0
            
            if num in dp:
                return dp[num]
            
            dp[num] = max(
                num,
                solve(num // 2) + solve(num // 3) + solve(num // 4)
            )
            
            return dp[num]
        
        return solve(n)