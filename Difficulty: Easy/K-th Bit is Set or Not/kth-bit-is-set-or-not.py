class Solution:
    def checkKthBit(self, n, k):
        # code here
        if n>>k & 1 ==1:
            return True
        else:
            return False
        