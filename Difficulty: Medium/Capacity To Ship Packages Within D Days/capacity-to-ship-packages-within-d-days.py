#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, n, d):
        # code here 
        def fun(arr,capacity):
            load = 0
            day =1
            for i in range(len(arr)):
                if load+arr[i]>capacity:
                    day = day+1
                    load = arr[i]
                else:
                    load+=arr[i]
            return day
        low=max(arr)
        high =sum(arr)
        while low<=high:
            mid = (low+high)//2
            ans = fun(arr,mid)
            if ans<=d:
                high = mid -1
            else:
                low = mid+1
        return low