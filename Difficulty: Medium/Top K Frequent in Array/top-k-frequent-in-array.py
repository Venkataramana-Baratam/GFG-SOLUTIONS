class Solution:
	def topKFreq(self, arr, k):
	    
	    
		mpp = {}
		for i in arr:
		    mpp[i] = mpp.get(i,0)+1
		res = []
		for key,value in mpp.items():
		    res.append((key,value))
	    res.sort(key= lambda x:(x[1],x[0]),reverse = True)
	    ans = [key for key,value in res[:k]]
	    return ans