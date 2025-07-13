class Solution:
    def maxChildren(self, greed, cookie):
        #Your code goes here.
        greed.sort()
        cookie.sort()
        j=0
        ans =0
        for i in range(len(greed)):
           while j<len(cookie):
               if cookie[j]>=greed[i]:
                   ans+=1
                   j+=1
                   break
               j+=1
        return ans