class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        def possible(stalls,dist,cows):
            cntcows =1
            last = stalls[0]
            for i in range(1,n):
                if stalls[i]-last>=dist:
                    cntcows+=1
                    last = stalls[i]
                if cntcows>=k:
                    return True
            return False
        stalls.sort()
        n = len(stalls)
        low =1
        high =stalls[n-1]-stalls[0]
        while low<=high:
            mid = (low+high)//2
            if possible(stalls,mid,k):
                low = mid+1
            else:
                high = mid-1
        return high
