from typing import List
import math

class Solution:
    def quadraticRoots(self, a: int, b: int, c: int) -> List[int]:
        
        d = b*b - 4*a*c
        
        # Imaginary roots
        if d < 0:
            return [-1]
        
        r1 = math.floor((-b + math.sqrt(d)) / (2*a))
        r2 = math.floor((-b - math.sqrt(d)) / (2*a))
        
        return [max(r1, r2), min(r1, r2)]