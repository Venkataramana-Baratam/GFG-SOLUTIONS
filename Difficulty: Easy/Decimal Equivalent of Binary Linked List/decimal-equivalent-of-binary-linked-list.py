# your task is to complete this function
# Function should return an integer value
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:

    def decimalValue(self, head):
        MOD = 10**9 + 7
        # Code here
        temp = head
        ans =[]
        while temp:
            ans.append(temp.data)
            temp = temp.next
        n = len(ans)
        num=0
        p1 = 1
        for i in range(n-1,-1,-1):
            if ans[i]==1:
                num = num+p1
            p1 = p1*2
        return num%MOD