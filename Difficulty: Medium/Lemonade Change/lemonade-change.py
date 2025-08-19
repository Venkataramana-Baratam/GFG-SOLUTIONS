#User function Template for python3
class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        five = 0
        ten = 0
        n = len(bills)
        for i in range(n):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five:
                    ten+=1
                    five-=1
                else:
                    return False
            else:
                if ten and five:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
                
                