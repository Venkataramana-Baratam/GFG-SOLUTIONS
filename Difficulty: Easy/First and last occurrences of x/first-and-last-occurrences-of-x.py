#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        # Code here
        if x not in arr:
            return [-1]
        n = len(arr)
        low = 0
        high = n-1
        res = []
        ans1 = n
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>=x:
                ans1 = mid
                high = mid -1
            else:
                low = mid+1
        res.append(ans1)
        ans2 = n
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>x:
                ans2 = mid
                high = mid -1
            else:
                low = mid+1
        res.append(ans2-1)
        return res