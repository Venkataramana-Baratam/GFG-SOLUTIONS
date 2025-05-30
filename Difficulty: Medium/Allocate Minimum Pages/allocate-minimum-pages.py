class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n =len(arr)
        if n<k:
            return -1
        def allocate(arr,page):
            student =1
            no_of_page=0
            for i in range(n):
                if no_of_page+arr[i]<=page:
                    no_of_page+=arr[i]
                else:
                    student+=1
                    no_of_page=arr[i]
            return student
        low =max(arr)
        high = sum(arr)
        while low<=high:
            mid =(low+high)//2
            no_of_student = allocate(arr,mid)
            if no_of_student>k:
                low = mid+1
            else:
                high = mid-1
        return low
                
