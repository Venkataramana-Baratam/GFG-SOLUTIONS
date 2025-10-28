
import heapq
class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        # code here
        res = []
        heap = []
        
        for i in range(min(len(arr1),k)):
            
            heapq.heappush(heap,(arr1[i]+arr2[0],i,0))
            
        while heap and len(res)<k:
            
            total,i,j = heapq.heappop(heap)
    
            res.append([arr1[i],arr2[j]])
        
            if j+1<len(arr2):
                
                heapq.heappush(heap,(arr1[i]+arr2[j+1],i,j+1))
        return res
