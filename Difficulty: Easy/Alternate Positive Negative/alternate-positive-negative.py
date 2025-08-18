#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos = []
        neg = []
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        i = 0
        j = 0
        k =0
        while i<len(pos) and j<len(neg):
            arr[k] = pos[i]
            i+=1
            k+=1
            arr[k] = neg[j]
            j+=1
            k+=1
        while i<len(pos):
            arr[k] = pos[i]
            i+=1
            k+=1
        while j<len(neg):
            arr[k] = neg[j]
            j+=1
            k+=1
        return arr
            