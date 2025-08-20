#User function Template for python3

class Solution:
    # Function to check if we can reach the last index from the 0th index.
    def canReach(self, arr):
        #code here
        
        max_index = 0
        for i in range(len(arr)):
            
            if i>max_index:
                return False
                
            max_index = max(max_index,i+arr[i])
        return True