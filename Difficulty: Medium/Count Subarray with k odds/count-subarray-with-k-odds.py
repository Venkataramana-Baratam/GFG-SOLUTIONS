class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        def nice(S):
            l = 0
            r =0
            cnt = 0 
            odd_count = 0
            n = len(arr)
            while r<n:
                if arr[r]%2!=0:
                    odd_count+=1
                while odd_count>S:
                    if arr[l]%2!=0:
                        odd_count-=1
                    l+=1
                cnt+=(r-l+1)
                r+=1
            return cnt
        return nice(k)-nice(k-1)