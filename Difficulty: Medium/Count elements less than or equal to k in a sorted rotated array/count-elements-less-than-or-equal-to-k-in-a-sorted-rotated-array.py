
from bisect import bisect_left,bisect_right
class Solution:
    def countLessEqual(self, arr, x):
        #code here
        
        pivot = 0
        for i in range(len(arr)-1):
            
            if arr[i]>arr[i+1]:
                pivot = i
                break
        arr1 = arr[:pivot+1]
        arr2 = arr[pivot+1:]
        n1 = len(arr1)
        n2 = len(arr2)
        ub1 = bisect_right(arr1,x)
        ub2 = bisect_right(arr2,x)
        
    
        return ub1+ub2