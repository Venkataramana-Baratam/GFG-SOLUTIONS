class Solution:
    def getMaxOccurringChar(self, s):
        # code here
        mpp = {}
        for i in s:
            mpp[i] = mpp.get(i, 0) + 1

        maxi = float('-inf')
        for val in mpp.values():
            maxi = max(maxi, val)

        ans = None
        for ch, val in mpp.items():
            if val == maxi:
                if ans is None or ch < ans:
                    ans = ch

        return ans
