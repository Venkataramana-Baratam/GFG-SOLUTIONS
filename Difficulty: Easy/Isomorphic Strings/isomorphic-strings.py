class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        
        if len(s1)!=len(s2):
            return False
            
        mpp1 = {}
        mpp2 = {}
         
        for i in range(len(s1)):
            
            char1 = s1[i]
            char2 = s2[i]
             
            if char1 in mpp1 and mpp1[char1]!=char2:
                 return False
                 
            if char2 in mpp2 and mpp2[char2]!=char1:
                 return False
                 
            mpp1[char1] = char2
            mpp2[char2] = char1
            
            
        return True