class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            index = i % n
            while stack and stack[-1] <= arr[index]:
                stack.pop()
            if stack:
                result[index] = stack[-1]
            stack.append(arr[index])
        return result
