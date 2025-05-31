class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        m  = len(arr[0])
    
        def lower_bound(arr,n,x):
            low = 0
            high = n-1
            ans = n
            while low<=high:
                mid =(low+high)//2
                if arr[mid]>=x:
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            return ans
        cnt_max = -sys.maxsize
        cnt_ones = 0
        index =-1
        for i in range(n):
            cnt_ones = m - lower_bound(arr[i],m,1)
            if cnt_ones>cnt_max:
                cnt_max = cnt_ones
                index = i
        return index