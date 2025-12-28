class Solution:
    def minTime(self, ranks, n):
        # code here
        
        def canMake(t):
            
            total = 0
            
            for r in ranks:
                
                time_spent = 0
                donut_no = 1
                
                while time_spent + donut_no*r<=t:
                    
                    time_spent += donut_no*r
                    donut_no +=1
                    total +=1
                    
                if total>=n:
                    return True
            return False
        
        low = 1
        high = max(ranks) * (n*(n+1)//2)
        while low<=high:
            mid = (low + high)//2
            
            if canMake(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans