class Solution:
	def mergeOverlap(self, arr):
		# Code here
		arr.sort(key = lambda x:x[0])
		res = [arr[0]]
		i =1
		n = len(arr)
		while i<n:
		    last = res[-1]
		    if arr[i][0]<=last[1]:
		        last[1] = max(last[1],arr[i][1])
		    else:
		        res.append(arr[i])
		    i+=1
		return res