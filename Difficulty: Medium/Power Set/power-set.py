# User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        
        temp = ""
        n = len(s)
        res = []
        
        def f(i, temp):
            if i == n:
                if temp != "":
                    res.append(temp)
                return
            temp += s[i]
            f(i + 1, temp)
            
            temp = temp[:-1]   # corrected: strings are immutable, so use slicing instead of -=
            f(i + 1, temp)
        
        f(0, temp)
        res.sort()
        return res
