#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        n = len(arr)
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]
        return arr[k-1]
        
        
