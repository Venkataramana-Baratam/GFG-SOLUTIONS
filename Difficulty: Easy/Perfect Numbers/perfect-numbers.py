class Solution:
    def isPerfect(self, n):
        # code here 
        if n == 1:
            return False  

        s = 1  
        i = 2

        while i * i <= n:
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n // i
            i += 1

        return s == n