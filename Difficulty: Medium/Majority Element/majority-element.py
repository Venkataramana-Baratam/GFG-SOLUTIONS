#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        n  =len(arr)
        mpp = {}
        for i in range(len(arr)):
            if arr[i] in mpp:
                mpp[arr[i]]+=1
            else:
                mpp[arr[i]]=1
        for key,value in mpp.items():
            if value>n//2:
                return key
        return -1