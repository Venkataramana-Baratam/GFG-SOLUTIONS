#User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1