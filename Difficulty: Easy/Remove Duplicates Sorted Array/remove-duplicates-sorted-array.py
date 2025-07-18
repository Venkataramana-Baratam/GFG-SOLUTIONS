class Solution:
    def removeDuplicates(self, arr):
        # code here 
        
        set1 = set(arr)
        result = list(set1)
        result.sort()
        return result