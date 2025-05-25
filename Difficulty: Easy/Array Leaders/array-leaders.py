class Solution:
    def leaders(self, arr):
        ans = []
        max_so_far = arr[-1]
        ans.append(max_so_far)
        
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= max_so_far:
                ans.append(arr[i])
                max_so_far = arr[i]
        
        return ans[::-1]  
