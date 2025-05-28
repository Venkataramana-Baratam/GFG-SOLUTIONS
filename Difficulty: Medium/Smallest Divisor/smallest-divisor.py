#User function Template for python3
import math
class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        low =1
        high =max(arr)
        while low<=high:
            mid =(low+high)//2
            total = sum(math.ceil(i/mid) for i in arr)
            if total<=k:
                high = mid-1
            else:
                low =mid+1
        return low