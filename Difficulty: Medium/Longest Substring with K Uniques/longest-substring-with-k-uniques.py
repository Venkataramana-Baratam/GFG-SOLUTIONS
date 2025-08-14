

from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        hash_map =defaultdict(int) 
        l = 0
        r = 0
        n = len(s)
        maxi = -1
        length = 0
        while r<n:
            hash_map[s[r]]+=1
            while len(hash_map)>k:
                hash_map[s[l]]-=1
                if hash_map[s[l]]==0:
                    del hash_map[s[l]]
                l+=1
            if len(hash_map)==k:
                length = r-l+1
                maxi = max(maxi,length)
            r+=1
        return maxi
        