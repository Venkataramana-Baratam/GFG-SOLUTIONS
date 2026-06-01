class Solution:
    def findMaxProduct(self, arr):
        count_negative = 0
        count_zero = 0
        min_negative = float('inf')

        product_without_zero = 1

        if len(arr) == 1:
            return arr[0]

        for num in arr:
            if num == 0:
                count_zero += 1
                continue

            if num < 0:
                count_negative += 1
                min_negative = min(min_negative, abs(num))

            product_without_zero *= num

        if count_zero == len(arr):
            return 0

        if product_without_zero > 0:
            return product_without_zero % (10 ** 9 + 7)

        if count_negative == 1 and count_zero + count_negative == len(arr):
            return 0

        return (product_without_zero // (-min_negative)) % (10 ** 9 + 7)