class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        ans = list(zip(val,wt))
        ans.sort(key = lambda x:x[0]/x[1],reverse = True)
        total = 0.0
        for v,w in ans:
            if w<=capacity:
                total+=v
                capacity-=w
            else:
                total+= (capacity/w)*v
                break
        return total