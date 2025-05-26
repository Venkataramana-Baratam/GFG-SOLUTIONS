class Solution:
    def findDuplicates(self, arr):
        # code here
        ans=[]
        mpp = {}
        for i in arr:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        for key,values in mpp.items():
            if values>1:
                ans.append(key)
                
        return ans