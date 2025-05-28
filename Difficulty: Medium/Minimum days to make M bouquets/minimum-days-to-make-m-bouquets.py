#User function Template for python3

class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        def possible(m,k,day,arr):
            cnt=0
            nbk=0
            for i in range(len(arr)):
                if arr[i]<=day:
                    cnt+=1
                else:
                    nbk+=(cnt//k)
                    cnt=0
            nbk+=(cnt//k)
            if nbk>=m:
                return True
            else:
                return False
        low=min(arr)
        high = max(arr)
        while low<=high:
            mid =(low+high)//2
            if len(arr)<m*k:
                return -1
            if possible(m,k,mid,arr):
                high = mid-1
            else:
                low = mid+1
        return low