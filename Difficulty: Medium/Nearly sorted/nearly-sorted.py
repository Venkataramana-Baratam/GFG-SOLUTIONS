
import heapq
class Solution:
    def nearlySorted(self, arr, k):  
        
        pq = []
        
        for num in arr:
            heapq.heappush(pq,num)
        i  = 0 
        while pq:
            
            arr[i] = heapq.heappop(pq)
            i+=1
        return arr