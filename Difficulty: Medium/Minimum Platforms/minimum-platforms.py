#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        n = len(arr)
        i =0
        j =0
        arr.sort()
        dep.sort()
        cnt =0
        maxi= 0
        while i<n:
            if arr[i]<=dep[j]:
                cnt+=1
                i+=1
            else:
                cnt-=1
                j+=1
            maxi = max(maxi,cnt)
        return maxi