

from bisect import bisect_left,bisect_right
class Solution:
    def cntInRange(self, arr, queries):
        # code here
        arr.sort()
        res = []
        for l,r in queries:
            
            left = bisect_left(arr,l)
            right = bisect_right(arr,r)
            res.append(right - left)
        return res
            