#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        mpp = {}
        l1= []
        arr.sort()
        n =len(arr)
        for i in arr:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i]=1
        for key,value in mpp.items():
            if value==2:
                l1.append(key)
        for i in range(1,n+1):
            if i not in mpp:
                l1.append(i)
                break
        return l1