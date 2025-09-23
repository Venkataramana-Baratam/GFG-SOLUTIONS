from collections import deque

class Solution:
    def reverseQueue(self, q):
        stack = []

        while q:  
            stack.append(q.popleft())
        while stack:
            q.append(stack.pop())
