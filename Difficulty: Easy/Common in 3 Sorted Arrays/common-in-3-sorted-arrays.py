#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)
        common = list(set1 & set2 & set3)
        common.sort()
        return common[:]