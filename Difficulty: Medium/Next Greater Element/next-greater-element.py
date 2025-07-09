class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        st = []
        res = [-1]*n
        for i in range(n-1,-1,-1):
            while st and st[-1]<=arr[i]:
                st.pop()
            if len(st)==0:
                res[i] = -1
            else:
                res[i] = st[-1]
            st.append(arr[i])
        return res
            