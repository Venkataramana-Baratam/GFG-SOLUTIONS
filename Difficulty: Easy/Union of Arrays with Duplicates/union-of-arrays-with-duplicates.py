#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        set1 = set(a)
        set2 = set(b)
        set3 = set(list(set1)+list(set2))
        ans = list(set3)
        return len(ans)