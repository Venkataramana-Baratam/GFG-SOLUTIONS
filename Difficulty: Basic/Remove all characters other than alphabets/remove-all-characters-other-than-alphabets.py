class Solution:
    def removeSpecialCharacter(self, S):
        s = ''
        for i in S:
            if i.isalpha():
                s += i
        return s if s!='' else -1
