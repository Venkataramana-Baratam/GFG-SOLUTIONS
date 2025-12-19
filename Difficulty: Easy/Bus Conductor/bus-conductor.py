class Solution:
    def findMoves(self, chairs, passengers):
        
        
        
        chairs.sort()
        passengers.sort()
        n = len(chairs)
        cnt = 0
        for i in range(n):
            cnt+=abs(chairs[i] - passengers[i])
            
        return cnt
        
