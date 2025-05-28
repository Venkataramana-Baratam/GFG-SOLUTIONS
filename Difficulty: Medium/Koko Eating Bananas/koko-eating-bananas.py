#User function Template for python3
import math
class Solution:
    def kokoEat(self,arr,k):
        # Code here
        low =1
        high =max(arr)
        ans = float('-inf')
        while low<=high:
            mid =(low+high)//2
            def fun(arr,h):
                req_hours = 0
                for  i in range(len(arr)):
                    req_hours+=math.ceil(arr[i]/h)
                return req_hours
            total_hours = fun(arr,mid)
            if total_hours<=k:
                ans = mid
                high = mid-1
            else:
                low=mid+1
        return ans
                