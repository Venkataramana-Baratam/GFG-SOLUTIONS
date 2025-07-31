#User function Template for python3
class Solution:

	def immediateSmaller(self, arr):
		# code here
		n = len(arr)
		for i in range(n-1):
		    if arr[i+1]<arr[i]:
		        arr[i] = arr[i+1]
		    else:
		        arr[i] = -1
		arr[n-1] = -1
		return arr