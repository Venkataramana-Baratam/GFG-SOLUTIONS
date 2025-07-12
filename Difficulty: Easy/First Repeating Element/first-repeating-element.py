class Solution:
    def firstRepeated(self, arr):
        mpp = {}
        for i in arr:
            if i in mpp:
                mpp[i] += 1
            else:
                mpp[i] = 1
        
        for idx, val in enumerate(arr):
            if mpp[val] > 1:
                return idx + 1  
        return -1
