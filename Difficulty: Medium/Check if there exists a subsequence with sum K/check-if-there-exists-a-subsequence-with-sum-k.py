class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        from functools import lru_cache
        
        @lru_cache(None)
        def f(i, s):
            if s == K:
                return True
            if i == N or s > K:  
                return False

            if f(i + 1, s + arr[i]):
                return True

            if f(i + 1, s):
                return True
            return False

        return f(0, 0)
