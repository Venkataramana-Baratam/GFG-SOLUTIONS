class Solution:
    def romanToDecimal(self, s): 
        # code here
        mpp = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)
        cnt= 0 
        for i in range(n):
            if i < n-1 and mpp[s[i]]<mpp[s[i+1]]:
                cnt -= mpp[s[i]]
            else:
                cnt += mpp[s[i]]
        return cnt        
        
            