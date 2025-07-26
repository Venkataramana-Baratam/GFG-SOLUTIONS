class Solution:
    def findMajority(self, arr):
        # code here
        mpp = {}
        n = len(arr)
        ans = []
        for i in arr:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] = 1
        for key,value in mpp.items():
            if value>n//3:
                ans.append(key)
        ans.sort()
        return ans
                