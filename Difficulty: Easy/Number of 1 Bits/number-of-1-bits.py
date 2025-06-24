#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		count =0
		while n>1:
		    if n%2==1:
		        count+=1
		    n = n//2
		if n==1:
		    count+=1
		return count