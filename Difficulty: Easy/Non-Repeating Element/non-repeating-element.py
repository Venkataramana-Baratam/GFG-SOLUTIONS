class Solution:
    def firstNonRepeating(self, arr): 
        mpp = {}
        
        for i in arr:
            mpp[i] = mpp.get(i, 0) + 1
        
        for i in arr:
            if mpp[i] == 1:
                return i
        
        return 0
