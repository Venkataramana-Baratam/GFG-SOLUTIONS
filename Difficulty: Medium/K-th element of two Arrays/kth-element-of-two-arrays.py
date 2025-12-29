class Solution:
    def kthElement(self, a, b, k):
        # code here
        
        res = a + b
        res.sort()
        return res[k-1]
        