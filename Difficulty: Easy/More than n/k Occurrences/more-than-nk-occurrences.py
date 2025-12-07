class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        #Your code here
        mpp = {}
        n = len(arr)
        for i in arr:
            
            mpp[i] = mpp.get(i,0) + 1
            
        cnt = 0
        for key,val in mpp.items():
            if val > n//k:
                cnt+=1
        return cnt
            