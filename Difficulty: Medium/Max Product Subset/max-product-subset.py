class Solution:
    def findMaxProduct(self, arr):
        # code here
        
        count_zeros = 0
        
        count_negative = 0
        
        product_without_zero = 1
        
        min_negative = float('inf')
        
        MOD = 10 ** 9 + 7
        
        if len(arr) == 1:
            return arr[0]
        for num in arr:
            
            if num == 0:
                
                count_zeros += 1
                continue
            
            if num < 0:
                
                count_negative += 1
                
                min_negative = min(min_negative , abs(num))
                
            product_without_zero *= num
            
        if count_zeros == len(arr):
            return 0
            
        if product_without_zero > 0:
            return product_without_zero % MOD
            
        if count_negative == 1 and count_negative + count_zeros == len(arr):
            return 0
            
        return (product_without_zero // (-min_negative)) % MOD
                