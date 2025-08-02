#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        # code here
        mpp = {}
        for i in arr:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        for key,value in mpp.items():
            if key==0:
                return value