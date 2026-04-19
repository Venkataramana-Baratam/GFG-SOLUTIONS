class Solution:
    def isPower(self, x, y):
        
        
        if x == 1:
            return y == 1
        
        power = 1
        
        while power < y:
            power *= x
        
        return power == y