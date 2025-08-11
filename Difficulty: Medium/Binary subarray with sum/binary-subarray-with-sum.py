class Solution:
    def numberOfSubarrays(self, arr, target):
        # code here
        def most(S):
            l = 0
            r =0 
            n = len(arr)
            sum1 = 0
            cnt =0
            if S<0:
                return 0
            while r<n:
                sum1+=arr[r]
                while sum1>S:
                    sum1-=arr[l]
                    l+=1
                cnt+=(r-l+1)
                r+=1
            return cnt
        return most(target)-most(target-1)