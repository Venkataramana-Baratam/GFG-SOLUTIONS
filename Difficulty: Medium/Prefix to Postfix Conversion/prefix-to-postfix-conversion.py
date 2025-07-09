#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        n  = len(pre_exp)
        i = n-1
        st = []
        while i>=0:
            if pre_exp[i].isalnum():
                st.append(pre_exp[i])
            else:
                t1= st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                st.append( t1 + t2+pre_exp[i])
            i-=1
        return st[-1]