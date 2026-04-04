class Solution:
    def graycode(self, n):
        result = []
        
        for i in range(1 << n): 
            gray = i ^ (i >> 1)
            result.append(format(gray, '0{}b'.format(n)))
        
        return result