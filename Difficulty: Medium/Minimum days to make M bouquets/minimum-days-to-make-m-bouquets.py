class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        n = len(arr)
        if m*k>n:
            return -1
        low =min(arr)
        high = max(arr)
        def possible(arr,x,m,k):
            cnt =0
            nbk  =0
            for i in range(n):
                if arr[i]<=x:
                    cnt+=1
                else:
                    nbk +=(cnt//k)
                    cnt =0
            nbk+=(cnt//k)
            if nbk>=m:
                return True
            return False
        while low<=high:
            mid  = (low+high)//2
            if possible(arr,mid,m,k):
                high = mid -1
            else:
                low = mid+1
        return low