class Solution:
    def kClosest(self, points, k):
        # code here
        
        x1,y1 = (0,0)
        res = []
        mpp = {}
        for x2,y2 in points:
            
            dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
            mpp[(x2,y2)] = dist
            
        sorted_points = sorted(mpp.items(), key=lambda x: x[1])
        
        res = [point for point, _ in sorted_points[:k]]
        
        return res    
           
    
        