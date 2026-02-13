#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        #code here
        
        mpp = {}
        
        for num in arr:
            
            mpp[num] = mpp.get(num,0) + 1
            
        for key,val in mpp.items():
            
            
            if val>1:
                return key