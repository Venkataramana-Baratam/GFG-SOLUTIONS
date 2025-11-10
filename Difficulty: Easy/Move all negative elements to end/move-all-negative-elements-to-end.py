class Solution:
    def segregateElements(self, arr):
        # Your corrected code
        pos = []
        neg = []
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        pos.extend(neg)
        for i in range(len(arr)):
            arr[i] = pos[i]
