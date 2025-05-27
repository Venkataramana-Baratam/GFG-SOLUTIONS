class Solution:
    def countFreq(self, arr, target):
        #code here
        mpp = {}
        for i in range(len(arr)):
            if arr[i] in mpp:
                mpp[arr[i]]+=1
            else:
                mpp[arr[i]] =1
        for key,value in mpp.items():
            if key==target:
                return value
        return 0