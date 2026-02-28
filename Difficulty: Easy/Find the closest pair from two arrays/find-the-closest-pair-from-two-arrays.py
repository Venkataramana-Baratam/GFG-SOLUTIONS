class Solution:
    def findClosestPair(self,arr1, arr2, x):
        #code here
        
        
        res = []
        
        min_diff = float('inf')
        
        i = 0
        j = len(arr2)-1
        
        while i<len(arr1) and j>=0:
            
            
            
            total = arr1[i] + arr2[j]
            
            diff  = abs(total - x)
            
            if diff<min_diff:
                
                min_diff = diff
                
                res = [arr1[i],arr2[j]]
                
            if total>x:
                j-=1
            else:
                i+=1
        return res