class Solution:
    def twoSum(self, arr, target):
        mpp = {}
        
        for i in range(len(arr)):
            moreneed = target - arr[i]
            
            if moreneed in mpp:
                return True
            else:
                mpp[arr[i]] = i
        
        return False