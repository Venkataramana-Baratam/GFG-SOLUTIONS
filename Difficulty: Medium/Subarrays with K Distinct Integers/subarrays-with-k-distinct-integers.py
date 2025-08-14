#User function Template for python3
from collections import defaultdict
class Solution:
    def exactlyK(self, arr, k):
        # Code here
        def atmost(k):
            l = 0
            cnt = 0
            mpp = defaultdict(int)
            for r in range(len(arr)):
                mpp[arr[r]]+=1
                while len(mpp)>k:
                    mpp[arr[l]]-=1
                    if mpp[arr[l]]==0:
                        del mpp[arr[l]]
                    l+=1
                cnt+=(r-l+1)
            return cnt
        return atmost(k)-atmost(k-1)