#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		n =len(mat)
		def binary_search(row,n,x):
		    low =0 
		    high =len(row)-1
		    while low<=high:
		        mid =(low+high)//2
		        if row[mid]==x:
		            return True
		        elif row[mid]<x:
		            low = mid+1
		        else:
		            high = mid-1
		    return False
		for i in range(n):
		    if binary_search(mat[i],n,x):
		        return True
		return False