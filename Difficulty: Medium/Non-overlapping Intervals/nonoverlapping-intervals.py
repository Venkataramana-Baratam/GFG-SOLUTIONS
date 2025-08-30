class Solution:
    def minRemoval(self, intervals):
        # code here
        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        i =1
        last = intervals[0]
        cnt =1
        while i<n:
            if last[1]<=intervals[i][0]:
                cnt+=1
                last = intervals[i]
            i+=1
        return n-cnt