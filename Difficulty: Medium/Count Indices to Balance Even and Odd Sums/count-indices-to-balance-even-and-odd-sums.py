class Solution:
    def cntWays(self, arr):
        # code here
        
        n = len(arr)
        total_even = 0
        total_odd = 0
        for i in range(n):
            if i%2==0:
                total_even+=arr[i]
            else:
                total_odd+=arr[i]
                
        left_even = 0
        left_odd = 0
        cnt = 0
        for i in range(n):
            
            if i%2==0:
                
                total_even-=arr[i]
            else:
                
                total_odd-=arr[i]
        
            if left_even + total_odd == left_odd + total_even:
                cnt+=1
            if i%2==0:
                
                left_even+=arr[i]
            else:
                left_odd+=arr[i]
                
        return cnt