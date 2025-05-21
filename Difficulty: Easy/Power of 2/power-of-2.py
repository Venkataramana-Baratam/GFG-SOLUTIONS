#User function Template for python3

class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # code here
        return True if n!=0 and n&(n-1)==0 else False