class Solution:
      def leftSmaller(self, arr):
          #code here 
        n = len(arr)
        res = [-1]*n
        st = []
        for i in range(n):
            while st and st[-1]>=arr[i]:
                st.pop()
            if len(st)==0:
                res[i] = -1
            else:
                res[i] = st[-1]
            st.append(arr[i])
        return res                