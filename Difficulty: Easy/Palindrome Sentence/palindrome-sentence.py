class Solution:
	def isPalinSent(self, s):
		# code here
		lower = ''.join(c for c in s.lower() if c.isalnum())
		return lower == lower[::-1]