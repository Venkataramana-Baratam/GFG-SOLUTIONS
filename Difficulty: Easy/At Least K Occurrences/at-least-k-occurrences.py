class Solution:
    def firstElementKTime(self, arr,k):
        # code here
        mpp = {}
        for i in arr:
            mpp[i] = mpp.get(i,0)+1
            if mpp[i]==k:
                return i
        return -1