#User function Template for python3

class Solution:
    def minPartition(self, N):
        coin_list = [1,2,5,10,20,50,100,200,500,2000]
        ans = []
        for i in range(len(coin_list)-1,-1,-1):
            while N>=coin_list[i]:
                N -=coin_list[i]
                ans.append(coin_list[i])
        return ans
        