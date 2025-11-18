#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        # code here
        
        seen = set()
        for i in s:
            if i in seen:
                return i
            seen.add(i)
        return "-1"