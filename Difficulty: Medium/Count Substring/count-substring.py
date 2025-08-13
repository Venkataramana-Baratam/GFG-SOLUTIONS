class Solution:
    def countSubstring(self, s):
        mpp = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        cnt = 0
        matched = 0  # number of chars with count > 0

        for right in range(len(s)):
            ch = s[right]
            if mpp[ch] == 0:  # first time seeing this char in current window
                matched += 1
            mpp[ch] += 1

            while matched == 3:  # all 'a','b','c' are present
                cnt += len(s) - right
                left_ch = s[left]
                mpp[left_ch] -= 1
                if mpp[left_ch] == 0: 
                    matched -= 1
                left += 1

        return cnt
