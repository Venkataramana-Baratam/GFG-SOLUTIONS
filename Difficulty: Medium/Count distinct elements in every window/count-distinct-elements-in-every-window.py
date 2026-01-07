class Solution:
    def countDistinct(self, arr, k):
        # Code here
        
        n = len(arr)
        dist_cnt = []
        mpp = {}
        for i in range(k):
            
            mpp[arr[i]] = mpp.get(arr[i],0)+1
            
        dist_cnt.append(len(mpp))
        
        for i in range(k,n):
            
            old = arr[i-k]
            mpp[old]-=1
            
            if mpp[old]==0:
                
                del mpp[old]
                
            mpp[arr[i]] = mpp.get(arr[i],0)+1
            dist_cnt.append(len(mpp))
        
        return dist_cnt