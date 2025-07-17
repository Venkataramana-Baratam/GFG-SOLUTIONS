class Solution:
    def removeDups(self, s):
        seen = set()
        result = ""
        for char in s:
            if char not in seen:
                seen.add(char)
                result += char
        return result
