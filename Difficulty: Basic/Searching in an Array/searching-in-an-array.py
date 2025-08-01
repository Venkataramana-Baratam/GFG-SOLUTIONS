
from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        n = len(arr)
        for i in range(n):
            if arr[i]==k:
                return i+1
        return -1