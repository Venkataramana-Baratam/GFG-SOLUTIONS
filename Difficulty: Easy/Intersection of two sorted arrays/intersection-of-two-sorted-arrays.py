class Solution:
    def intersection(self, arr1, arr2):
        
        
        res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1
                j += 1
        return res