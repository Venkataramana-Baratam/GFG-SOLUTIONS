class Solution:
    def findPermutation(self, s):
        n = len(s)
        ds = []
        freq = [0] * n
        ans = set()   

        def f(ds, freq, ans):
            if len(ds) == n:
                ans.add("".join(ds))   
                return

            for i in range(n):
                if freq[i] == 0:
                    freq[i] = 1
                    ds.append(s[i])
                    f(ds, freq, ans)
                    ds.pop()
                    freq[i] = 0

        f(ds, freq, ans)
        return list(ans) 
