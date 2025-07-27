
class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        for i in s:
            if i=='(' or i=='[' or i=='{' :
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                it = stack[-1]
                stack.pop()
                if (i==']' and it =='[') or (i=='}' and it == '{') or (i==')' and it == '('):
                    continue
                else:
                    return False
        return len(stack)==0