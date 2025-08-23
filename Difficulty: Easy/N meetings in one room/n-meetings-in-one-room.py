#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        
        n = len(start)
        meetings = sorted([(end[i], start[i], i+1) for i in range(n)])
        
        free_time = -1
        cnt = 0
        ans =[]
        for e,s,idx in meetings:
            if s>free_time:
               cnt+=1
               free_time =e
               ans.append(idx)
        return cnt