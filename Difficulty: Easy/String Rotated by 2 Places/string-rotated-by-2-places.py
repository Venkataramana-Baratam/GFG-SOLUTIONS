class Solution:
    def isRotated(self, s1, s2):
        if len(s1) != len(s2):
            return False

        n = len(s1)

        anti_clock = s1[2:] + s1[:2]
        clock = s1[n-2:] + s1[:n-2]

        return anti_clock == s2 or clock == s2
