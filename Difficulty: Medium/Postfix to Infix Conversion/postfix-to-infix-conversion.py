#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        i = 0
        n = len(postfix)
        st = []
        while i<n:
            if postfix[i].isalnum():
                st.append(postfix[i])
            else:
                t1 = st[-1]
                st.pop()
                t2 = st[-1]
                st.pop()
                con = '(' + t2 + postfix[i] + t1 + ')'
                st.append(con)
            i+=1
        return st[-1]
            