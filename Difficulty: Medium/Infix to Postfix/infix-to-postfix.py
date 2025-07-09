class Solution:
    def InfixtoPostfix(self, s):
        #code here
        n = len(s)
        i =0
        st = []
        ans =""
        
        def priority(x):
            
            if x=='^':
                return 3
            if x=='*' or x=='/':
                return 2
            if x=='+' or x=='-':
                return 1
            return -1
            
        while i <n:
            if (s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z') or (s[i]>='0' and s[i]<='9'):
                ans = ans+s[i]
            elif(s[i]=='('):
                st.append(s[i])
            elif(s[i]==')'):
                while st and st[-1]!='(':
                    ans+=st[-1]
                    st.pop()
                st.pop()
            else:
                while st and priority(s[i])<=priority(st[-1]):
                    ans+=st[-1]
                    st.pop()
                st.append(s[i])
            i+=1
        while st:
            ans+=st[-1]
            st.pop()
            
        return ans