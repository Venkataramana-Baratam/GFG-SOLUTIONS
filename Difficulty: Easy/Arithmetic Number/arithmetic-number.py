class Solution:
    def inSequence(self, a, b, c):

        # Case: common difference is zero
        if c == 0:
            return 1 if b == a else 0

        # Check divisibility
        if (b - a) % c == 0:
            n = (b - a) // c
            if n >= 0:
                return 1

        return 0
