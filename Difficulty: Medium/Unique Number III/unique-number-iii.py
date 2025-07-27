#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        mpp = {}
        for i in arr:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        for key,value in mpp.items():
            if value==1:
                return key