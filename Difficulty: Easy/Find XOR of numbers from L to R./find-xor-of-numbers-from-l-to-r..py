class Solution:
    def findXOR(self, l, r):
        def fun1(n):
            if n % 4 == 0:
                return n
            elif n % 4 == 1:
                return 1
            elif n % 4 == 2:
                return n + 1
            else:  # n % 4 == 3
                return 0
        return fun1(r) ^ fun1(l-1)
