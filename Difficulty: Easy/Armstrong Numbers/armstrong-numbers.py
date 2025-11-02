#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        val = 0
        for i in str(n):
            
            val+=int(i)**3
        return val==n