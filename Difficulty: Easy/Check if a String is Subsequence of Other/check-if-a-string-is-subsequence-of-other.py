class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        i = 0
        j = 0
        while i<n and j<m:
            if s1[j]==s2[i]:
                j+=1
            i+=1
        return j==m
            
