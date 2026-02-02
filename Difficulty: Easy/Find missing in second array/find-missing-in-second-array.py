class Solution:
    def findMissing(self, a, b):
        present = [0] * 100001
        
        for x in b:
            present[x] = 1
        
        res = []
        for x in a:
            if present[x] == 0:
                res.append(x)
        
        return res
