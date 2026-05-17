class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:

        res = []

        for num in arr:

            if res and ((res[-1] >= 0 and num < 0) or
                        (res[-1] < 0 and num >= 0)):

                res.pop()

            else:
                res.append(num)

        return res