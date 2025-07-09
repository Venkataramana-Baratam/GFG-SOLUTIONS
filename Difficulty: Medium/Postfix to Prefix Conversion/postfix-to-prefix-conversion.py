#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        i = 0
        n = len(post_exp)
        st = []
        while i<n:
            if post_exp[i].isalnum():
                st.append(post_exp[i])
            else:
                t1 = st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                st.append(post_exp[i]+t2+t1)
            i+=1
        return st[-1]