class Solution:
    def generateBinary(self, n):
        # code here
        
        res = []
        for i in range(1,n+1):
            res.append(bin(i)[2:])
        return res