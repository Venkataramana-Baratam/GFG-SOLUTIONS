#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	j = -1
    	for i in range(len(arr)):
    	    if arr[i]==0:
    	        j = i
    	        break
    	if j==-1:
    	    return arr
    	for i in range(j+1,len(arr)):
    	    if arr[i]!=0:
    	        arr[i],arr[j] = arr[j],arr[i]
    	        j+=1
        return arr