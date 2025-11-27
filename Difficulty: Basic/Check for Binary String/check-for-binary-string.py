# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        
        for i in s:
            if i!='0' and i!='1':
                return False
        return True