class Solution:
    def findEvenOccurrences(self, arr):
        # code here
        
        mpp = {}
        
        for num in arr:
            
            mpp[num] = mpp.get(num,0) + 1
            
        
        res = []
        
        for key,val in mpp.items():
            
            if val % 2 == 0:
                res.append(key)
                
        return res if len(res)>0 else [-1]
