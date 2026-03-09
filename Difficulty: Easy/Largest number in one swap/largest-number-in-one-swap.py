class Solution:
    def largestSwap(self, s):
        res = list(s)
        for i in range(len(res)):
            target_idx = i
            for j in range(len(res) - 1, i, -1):
                if res[j] > res[target_idx]:
                    target_idx = j
            
            if target_idx != i:
                res[i], res[target_idx] = res[target_idx], res[i]
                return "".join(res)
        return s
