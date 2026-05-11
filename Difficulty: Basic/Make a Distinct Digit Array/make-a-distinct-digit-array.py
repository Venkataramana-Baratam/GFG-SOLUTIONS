#User function Template for python3

class Solution:
	def common_digits(self, nums):
		# Code here
		res = []
		
		for num in nums:
		    
		    for ch in str(num):
		        
		        res.append(int(ch))
		        
	    return sorted(list(set(res)))