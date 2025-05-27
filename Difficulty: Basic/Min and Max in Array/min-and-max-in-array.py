#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        maxi = arr[0]
        for i in range(1,len(arr)):
            if maxi<arr[i]:
                maxi = arr[i]
        mini = arr[0]
        for i in range(1,len(arr)):
            if mini>arr[i]:
                mini =arr[i]
        return mini,maxi