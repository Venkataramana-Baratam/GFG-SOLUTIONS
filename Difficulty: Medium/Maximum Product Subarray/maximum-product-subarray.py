class Solution:
	def maxProduct(self,arr):
		# code here
		
		maxi = -10**9

        prefix = 1
        suffix = 1
        n = len(arr)
        for i in range(n):
            prefix = (prefix or 1)*arr[i]
            suffix = (suffix or 1)*arr[n-1-i]
            maxi = max(prefix,suffix,maxi)
        return maxi