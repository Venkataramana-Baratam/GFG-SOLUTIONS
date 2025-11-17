class Solution:
    def findExtra(self,a,b):
        #add code here
        for i in range(len(a)):
            if a[i] not in b:
                return i
                