class Solution:
    def sort012(self, arr):
        # code here
        
        
        n = len(arr) 
        zeros = 0
        ones = 0
        twos = 0
        for num in arr:
            if num==0:
                zeros+=1
            elif num==1:
                ones+=1
            else:
                twos+=1
        i = 0
        while zeros>0:
            arr[i] = 0
            i+=1
            zeros-=1
        while ones>0:
            arr[i] = 1
            i+=1
            ones-=1
        while twos>0:
            arr[i] = 2
            i+=1
            twos-=1
        